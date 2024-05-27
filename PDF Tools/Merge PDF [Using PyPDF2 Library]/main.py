# import required libraries
import os
from PyPDF2 import PdfWriter

# current directory
path = "C:\\Users\\mainp\\OneDrive\\Computer Science and Engineering\\Programming\\Programming Languages\\Python\\Projects\\Python-Projects\\Beginner Projects\\Merge PDF [Using PyPDF2 Library]"

# list of files in the directory
files = os.listdir(path)

# list of pdf files
pdfs = []

# append pdf files to pdfs list
for file in files:
    if file.endswith('.pdf'):
        pdfs.append(file)

# merge pdf files
merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

# write merged pdf to file
merger.write("result.pdf")
merger.close()
