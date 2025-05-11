import fitz

from main import DEPARTMENT

def extract_name_town_pairs(pdf_path):
    doc = fitz.open(pdf_path)
    all_results = []

    for page in doc:
        words = page.get_text("words")
        page_width = page.rect.width
        midpoint = page_width / 2

        left_words = [w for w in words if w[0] < midpoint]
        right_words = [w for w in words if w[0] >= midpoint]

        def group_by_line(words):
            lines = {}
            for x0, y0, x1, y1, word, *_ in words:
                y_key = round(y0, 1)
                if y_key not in lines:
                    lines[y_key] = []
                lines[y_key].append((x0, word))
            return lines

        def split_by_largest_gap(line):
            if len(line) < 2:
                return "", ""

            line = sorted(line)
            gaps = [
                (line[i+1][0] - line[i][0], i)
                for i in range(len(line) - 1)
            ]
            if not gaps:
                return "", ""

            largest_gap, split_index = max(gaps)
            left_part = " ".join(w for x, w in line[:split_index+1])
            right_part = " ".join(w for x, w in line[split_index+1:])
            return left_part.strip(), right_part.strip()

        def extract_from_column(words):
            results = []
            lines = group_by_line(words)
            for y in sorted(lines):
                line = lines[y]
                name, town = split_by_largest_gap(line)
                if name and town:
                    results.append(f"{name} - {town}")
            return results

        all_results.extend(extract_from_column(left_words))
        all_results.extend(extract_from_column(right_words))

    return all_results

if __name__ == "__main__":
    pdf_path = "tmp/index.pdf"
    entries = extract_name_town_pairs(pdf_path)
    with open(f"data/inputs/{DEPARTMENT}/{DEPARTMENT}-characters.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(entries))

    with open(f"./data/inputs/{DEPARTMENT}/{DEPARTMENT}-characters.txt", 'r', encoding="utf-8-sig") as file:
        for line in file:
            if not line.split()[0].isupper():
                print(line)

    