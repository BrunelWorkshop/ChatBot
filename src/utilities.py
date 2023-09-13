from io import BytesIO

from PyPDF2 import PdfReader


def pdf_to_text(uploaded_pdf, st):
    text = ""
    try:
        with BytesIO(uploaded_pdf.read()) as pdf_bytes:
            pdf_reader = PdfReader(pdf_bytes)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
    return text


def split_text(text, max_tokens=2049):
    segments = []
    current_segment = ""
    tokens = text.split()
    for token in tokens:
        if len(current_segment) + len(token) + 1 <= max_tokens:
            current_segment += token + " "
        else:
            segments.append(current_segment.strip())
            current_segment = token + " "
    segments.append(current_segment.strip())
    return segments
