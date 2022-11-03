# importing Python Modules
import PyPDF2

Pdf_File= open("C:/udemyPython+Project+to+convert+Video+to+Gif+Format", "rb")
PDF_Reader = PyPDF2.PdfFileReader(Pdf_File)
Text = PDF_Reader.getPage(0).extractText()
print(Text)
