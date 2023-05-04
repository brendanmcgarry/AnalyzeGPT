import re
import platform


def clean_text(text):
    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    
    # Replace multiple newlines (with optional spaces or tabs) with a single newline
    text = re.sub(r'[\n\r]+[\s\t]*[\n\r]+', '\n', text)
    
    return text


def handle_windows_encoding(text):
    if platform.system() == 'Windows':
        text = text.encode('cp1252', errors='ignore').decode('cp1252')
    return text
