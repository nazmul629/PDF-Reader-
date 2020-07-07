import pyttsx3
import PyPDF2

robot = pyttsx3.init()
robot.setProperty('rate', 140) 
robot.setProperty('volume', 0.7) 


book = open('TheOneMinuteManager.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

print(pages)

for i in range(0,pages):
    readPage = pdfReader.getPage(i)
    text = readPage.extractText()
    robot.say(text)
    robot.runAndWait()

