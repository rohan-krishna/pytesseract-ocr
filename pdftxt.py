from os import name
from re import split
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def split_pages(path = "", name_of_split = ""):
    pdf = PdfFileReader(path)

    if pdf.isEncrypted:
        pdf.decrypt('')


if __name__ == '__main__':
    path = os.path.abspath('positive.pdf')
    # print(path)
    split_pages(path, 'chapter20')