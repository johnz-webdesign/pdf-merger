from PyPDF2 import PdfMerger

# Put PDFs here
pdf_files = ["1st-page.pdf", "2nd-page.pdf"]

merger = PdfMerger()

# Loop through and add PDFs
for pdf in pdf_files:
    merger.append(pdf)

# Output the merged file
merger.write("merged_pdf.pdf")
merger.close()

print("PDFs merged successfully")

# to run:
# python merge_pdfs.py