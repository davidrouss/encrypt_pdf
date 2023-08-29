import pdfkit


BINAIRE = r'/usr/bin/wkhtmltopdf'
CONFIG = pdfkit.configuration(wkhtmltopdf=BINAIRE)
OUTPUT = "/home/david/result.pdf"
ENCRYPTED_FILE = "/home/david/encrypted_PDF.pdf"
