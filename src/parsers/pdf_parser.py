import io
import re
import requests
import argparse
from pdfminer.converter import TextConverter
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

from utils.pdf_specific_cleaning import clean_text, handle_windows_encoding


def download_pdf(url):
    response = requests.get(url)
    return io.BytesIO(response.content)

def pdf_to_plaintext(pdf_io):
    output_io = io.StringIO()
    laparams = LAParams()
    extract_text_to_fp(pdf_io, output_io, laparams=laparams, output_type='text', codec='utf-8')
    return output_io.getvalue()

def parse_pdf(url):
    pdf_io = download_pdf(url)
    raw_text = pdf_to_plaintext(pdf_io)
    cleaned_text = clean_text(raw_text)
    cleaned_text = handle_windows_encoding(cleaned_text)
    return cleaned_text

def main():
    parser = argparse.ArgumentParser(description='Convert a PDF file from a URL to plaintext.')
    parser.add_argument('url', metavar='url', type=str, help='The URL of the PDF file to convert.')

    args = parser.parse_args()
    url = args.url

    cleaned_plaintext = parse_pdf(url)
    print(cleaned_plaintext.encode('cp1252', errors='ignore').decode('cp1252'))

if __name__ == "__main__":
    main()


# url = 'https://cosmos.surrey.ca/geo_ref/Images/Zoning/BYL_Zoning_12000.pdf'
