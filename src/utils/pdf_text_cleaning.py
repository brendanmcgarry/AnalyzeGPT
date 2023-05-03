import re
import platform

def clean_text(text):
    # TODO: Don't remove all newlines.
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(\w)-\s', r'\1', text)
    text = re.sub(r' {2,}', ' ', text)
    return text

def handle_windows_encoding(text):
    if platform.system() == 'Windows':
        text = text.encode('cp1252', errors='ignore').decode('cp1252')
    return text
