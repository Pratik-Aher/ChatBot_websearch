import os
from PyPDF2 import PdfReader

def load_text_from_file(file):
    """Load text from txt, md, or pdf"""
    ext = os.path.splitext(file.name)[-1].lower()
    if ext in [".txt", ".md"]:
        return file.read().decode("utf-8")
    elif ext == ".pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def recursive_character_splitter(text, chunk_size=1000, chunk_overlap=150):
    """Split text into chunks with overlap"""
    chunks, start, n = [], 0, len(text)
    while start < n:
        end = min(start + chunk_size, n)
        chunks.append(text[start:end])
        start = max(end - chunk_overlap, start + 1)
    return chunks
