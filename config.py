import pdfkit


BINAIRE = r'/usr/bin/wkhtmltopdf'
CONFIG = pdfkit.configuration(wkhtmltopdf=BINAIRE)
OUTPUT = "your_choice.pdf"
ENCRYPTED_FILE = "your_choice.pdf"
