from docx2pdf import convert

# specify the input Word file path
input_file = "sample_file.docx"

# specify the output PDF file path
output_file = input_file.replace(".docx", ".pdf")

# convert the Word document to PDF format
convert(input_file, output_file)
