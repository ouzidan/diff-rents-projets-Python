# importing Python Modules
#PyPDF2 ... pip install PyPDF2
#pyttsx3 .. pip install pyttsx3

import PyPDF2
import pyttsx3

Engine = pyttsx3.init()
PDF_Reader = PyPDF2.PdfFileReader(open("What is python.pdf", "rb"))
for Page_num in range(PDF_Reader.numPages):
    Text = PDF_Reader.getPage(Page_num).extractText()
    #Engine.say(Text)
    #Engine.runAndWait()
    Engine.save_to_file(Text, "audio.mp3")
    Engine.runAndWait()
