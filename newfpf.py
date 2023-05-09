# Content
fileName = "MyDoc.pdf"
def drawMyRuler(pdf):
    pdf.drawString(100,810, "x100")
    pdf.drawString(200,810, "x200")
    pdf.drawString(300,810, "x300")
    pdf.drawString(400,810, "x400")
    pdf.drawString(500,810, "x500")


    pdf.drawString(10,100, "y100")
    pdf.drawString(10,200, "y200")
    pdf.drawString(10,300, "y300")
    pdf.drawString(10,400, "y400")
    pdf.drawString(10,500, "y500")
    pdf.drawString(10,600, "y600")
    pdf.drawString(10,700, "y700")
    pdf.drawString(10,800, "y800")
    


documentTitle = "Document title"
title = "Tasmanian devil"

subTitle = "The Largest canivorous marsupial"

textLines = ["The tasmania devel (srapien) is",
"A crnevvvvrrrooo", "Daybreak."
]

# image = "thumb-removebg-preview1.png"

#Create document
from reportlab.pdfgen import canvas

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)




drawMyRuler(pdf)
#Title :: Set Fonts
# for font in pdf.getAvailableFonts():
#     print(font)
pdf.setFont("Courier-Bold",36)
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# pdfmetrics.registerFont(TTFont("abc", "sakBunderan.ttf"))
# pdf.setFont("abc", 36)

pdf.drawCentredString(300, 770, title)


#sub Title
pdf.setFillColorRGB(0,0,255)
pdf.setFont("Helvetica-Bold", 24)
pdf.drawCentredString(290,720,subTitle)

#Draw a line
pdf.line(30,70,550, 710) # Here its Horizontal line

# Text object :: for large amounts of text
from reportlab.lib import colors


text = pdf.beginText(40,680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)

# Draw a image
# pdf.drawInlineImage(image, 130, 400)
pdf.save()

