from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into a single PDF.

    Args:
        pdf_files (list): List of file-like objects or file paths of PDFs to merge.
        output_path (str): Path to save the merged PDF.

    Returns:
        None
    """
    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, 'wb') as out_file:
        writer.write(out_file)
