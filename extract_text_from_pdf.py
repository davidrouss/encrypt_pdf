import sys
import re
import config

from py_pdf_parser.loaders import load_file


def get_text_by_word_filtering(word) -> list:
    cves = []
    try:

        # Load PDF file
        pdf_file = load_file(config.PDF_FILE)
        
        # Get CVE elements ist
        elements = document.elements.filter_by_text_contains(word)
        
        # Loop on elements list
        for element in elements:

            # Get only CVE without other text
            cves_regex = re.findall('(CVE.[0-9]+-[0-9]+)',element.text())

            # Loop on CVE array
            for cve in cves_regex:
                cves.append(cve)
        
        return cves

    except(Exception,) as error: 
        print(error)

if __name__ == "__main__":

    get_text_by_word_filtering(sys.argv[1])
