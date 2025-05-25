from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_file, start_page, end_page, output_path):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    with open(output_path, "wb") as f:
        writer.write(f)
