import platform

def parse_pdf(url):
    pdf_io = download_pdf(url)
    raw_text = pdf_to_plaintext(pdf_io)
    cleaned_text = clean_text(raw_text)

    if platform.system() == 'Windows':
        cleaned_text = cleaned_text.encode('cp1252', errors='ignore').decode('cp1252')

    return cleaned_text
