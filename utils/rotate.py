from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(input_file, angle, output_path):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
