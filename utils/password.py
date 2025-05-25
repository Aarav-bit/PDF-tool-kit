from PyPDF2 import PdfReader, PdfWriter

def add_password(input_file, password, output_path):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    with open(output_path, "wb") as f:
        writer.write(f)

def remove_password(input_file, password, output_path):
    reader = PdfReader(input_file)
    if reader.is_encrypted:
        reader.decrypt(password)

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
