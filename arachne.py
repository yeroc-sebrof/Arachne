import os
import random

# If user didn't pip install PyPDF2
try:
     from PyPDF2 import PdfFileReader, PdfFileWriter
except:
     print("Need to install a pip package for PDF manipulation, follow the req.txt")
     exit(1)

debug = True

# Will include argparse later - Want to have both however
filename = input("Name the PDF you would like to encrypt ")

if not os.path.isfile("%s/%s" % (os.getcwd(), filename)):
     print("File you requested could not be found")
     if debug:
          print("Tried %s/%s" % (os.getcwd(), filename))
     exit(2)

# Will include argparse later
nPDF = int(input("How many PDFs do you need? "))

if nPDF < 0 or nPDF > 60:
     print("Something went wrong here")
     exit(3)

# init var
pdfin = PdfFileReader(filename)
pdfout = PdfFileWriter()

# read in the PDF
for page in range(pdfin.getNumPages()):
     pdfout.addPage(pdfin.getPage(page))

# For PDFs requried crypto'd
for copy in range(nPDF):
     password = ''
     for character in range(20): # Change this for longer pass
          password += (chr(random.randint(49,122)))

     pdfout.encrypt(password) # replace pdfout's content with a new encrypted PDF

     with open('pdf%i.pdf' % copy, 'wb') as out:
          pdfout.write(out)

     print("PDF%i's password = %s" % (copy, password)) # put this in a file later
