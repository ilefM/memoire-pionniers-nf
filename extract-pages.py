from pypdf import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Note: pages are 0-indexed
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    with open(output_pdf, "wb") as f:
        writer.write(f)

extract_pages("archives/8.pdf", "tmp/index.pdf", 74, 75)