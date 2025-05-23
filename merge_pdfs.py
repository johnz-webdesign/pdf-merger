from PyPDF2 import PdfMerger
import glob
import os

# Automatically find all PDF files in the current directory
pdf_files = glob.glob("*.pdf")

# Remove the output file from the list if it exists (to avoid merging it into itself)
output_filename = "merged_pdf.pdf"
if output_filename in pdf_files:
    pdf_files.remove(output_filename)

# Sort the files alphabetically for consistent ordering
pdf_files.sort()

if not pdf_files:
    print("No PDF files found in the current directory")
    exit()

print(f"Found {len(pdf_files)} PDF files to merge:")
for pdf in pdf_files:
    print(f"  - {pdf}")

merger = PdfMerger()

# Loop through and add PDFs
for pdf in pdf_files:
    try:
        merger.append(pdf)
        print(f"Added: {pdf}")
    except Exception as e:
        print(f"Error adding {pdf}: {e}")

# Output the merged file
merger.write(output_filename)
merger.close()

print(f"PDFs merged successfully into {output_filename}")

# to run:
# python merge_pdfs.py