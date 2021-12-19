"""
Welcome to Coder Mohit
Author - Mohit Goyal
Project Name - Text to PDF Converter
Source Code Link - www.TechyCodes.tech
Website - TechyCodes.tech
"""

# Import Necessary Libraries & Modules,

from fpdf import FPDF

# install it by using pip install fpdf
import os

# Now Create a Object of FPDF class

pdf = FPDF()

# Create or Add a page in PDF
pdf.add_page()

# Set font style and size for text
pdf.set_font('arial', size=10)

# Create Cells and Insert text in PDF

# Now, Left aligned Text
pdf.cell(200, 10, txt="Line 1 (Left aligned Text)", ln=1, align='L')

# For Center Align the text in PDF
pdf.cell(200, 10, txt="Line 2 (Center aligned Text)", ln=1, align='C')

# For Right Align Text
pdf.cell(200, 10, txt="Line 3 (Right Aligned Text)", ln=1, align='R')

# Save the PDF With any_name.pdf
pdf.output('Techy_Codes.pdf')

# Now the Coding is finished, Lets run the Code.
