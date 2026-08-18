from pypdf import PdfReader


def extract_pdf_text(file):
    """
    Extract text from a PDF file.

    Args:
        file: Streamlit UploadedFile object

    Returns:
        str: Extracted text from the PDF
    """
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()