
# merge pdf files
merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

# write merged pdf to file
merger.write("result.pdf")
merger.close()