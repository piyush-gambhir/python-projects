from pdf2docx import Converter
from docx2pdf import convert

def convert_pdf_to_docx(pdf_path, docx_path):
    # create a pdf converter object
    cv = Converter(pdf_path)

    # process the pdf
    cv.convert(docx_path, start=0, end=None)

    # close the pdf converter object
    cv.close()

def convert_docx_to_pdf(docx_path, pdf_path):
    convert(docx_path, pdf_path)


# Test the functions
# convert_docx_to_pdf('sample.docx', 'output.pdf')
convert_pdf_to_docx('output.pdf', 'output.docx')
