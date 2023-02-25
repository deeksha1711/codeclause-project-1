import os
import PyPDF2
import docx

#open the pdf file
pdf_file = open('example.pdf','rb')

#Read the pdf file
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

#Extract the text from the pdf file 
text = ''
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text += page.extractText()

#Create a new Word document
doc = docx.Document()

#Add the extracted text tothe word document
doc.add_paragraph(text)

#Save the Word document
doc.save('example.docx')

#Close the pdf file
pdf_file.close() 