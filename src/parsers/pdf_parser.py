import io
import requests
from pdfminer.converter import TextConverter
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

from ..utils import converted_text_cleaning


def download_pdf(url):
    response = requests.get(url)
    return io.BytesIO(response.content)

def pdf_to_plaintext(pdf_io):
    output_io = io.StringIO()
    laparams = LAParams()
    extract_text_to_fp(pdf_io, output_io, laparams=laparams, output_type='text', codec='utf-8')
    return output_io.getvalue()

def parse_pdf(file_path):
    raw_text = extract_text_from_pdf(file_path)
    cleaned_text = general_cleaning.clean_text(raw_text)
    return cleaned_text

url = 'https://cosmos.surrey.ca/geo_ref/Images/Zoning/BYL_Zoning_12000.pdf'
pdf_io = download_pdf(url)
plaintext = pdf_to_plaintext(pdf_io)

# Ignoring non-encodable characters when printing to console or redirecting the output to a file
print(plaintext.encode('cp1252', errors='ignore').decode('cp1252'))  # TODO: Move into parse_pdf fun; only use when system is Windows
