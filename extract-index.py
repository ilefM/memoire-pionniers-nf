import fitz  # PyMuPDF

def extract_name_town_pairs(pdf_path):
    doc = fitz.open(pdf_path)
    all_results = []

    for page in doc:
        words = page.get_text("words")  # list of (x0, y0, x1, y1, "word", ...)
        page_width = page.rect.width
        midpoint = page_width / 2

        # Split into left and right main columns
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
            """Split a line of (x, word) into two parts at largest gap"""
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

# Example usage
if __name__ == "__main__":
    pdf_path = "tmp/index.pdf"
    entries = extract_name_town_pairs(pdf_path)
    for entry in entries:
        print(entry)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(entries))