import pdfkit
import config
import sys

from PyPDF2 import PdfReader, PdfWriter


def convert_html_to_pdf(url: str) -> None:
    try: 
        pdfkit.from_url(url, output_path=config.OUTPUT, configuration=config.CONFIG)
        print("Conversion OK!")

    except(Exception,) as error:
        print(error)



def encrypt_with_password(password: str) -> None:
    reader = PdfReader(config.OUTPUT)
    writer = PdfWriter()

    try:
        for page in reader.pages:
            writer.add_page(page)
    
        writer.encrypt(password)

    except(Exception,) as error:
        print(error)

    try:
        with open(config.ENCRYPTED_FILE, "wb") as encrypted_file:
            writer.write(encrypted_file)

        print("Pdf encrypted ! ")

    
    except(Exception,) as error:
        print(error)

if __name__ == "__main__":
    pdf = convert_html_to_pdf(sys.argv[1])
    encrypt_with_password(sys.argv[2])
  
