# !/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import textwrap
import os, sys, time

from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)

day = input("Enter day: ")
can.drawString(100, 630.2060642678908, day)

date = input("Enter Date: ")
can.drawString(380.64999, 630.2060642678908, date)

description = input("Describe what did you do: ")
if len(description) > 80:
    wrap_description = textwrap.wrap(description,
                                     width=80,
                                     break_on_hyphens=False)
    can.drawString(73.25, 580.7060642678908, wrap_description[0])
    can.drawString(73.25, 560.7060642678908, wrap_description[1])
    can.drawString(73.25, 540.7060642678908, wrap_description[2])
    can.drawString(73.25, 520.7060642678908, wrap_description[3])
    can.drawString(73.25, 500.7060642678908, wrap_description[4])
else:
    can.drawString(73.25, 580.7060642678908, description)

activities = input("What is the activities / work produced: ")
if len(activities) > 80:
    wrap_activities = textwrap.wrap(activities,
                                    width=80,
                                    break_on_hyphens=False)
    can.drawString(73.25, 450.45606426789084, wrap_activities[0])
    can.drawString(73.25, 430.45606426789084, wrap_activities[1])
    can.drawString(73.25, 410.45606426789084, wrap_activities[2])
    can.drawString(73.25, 380.45606426789084, wrap_activities[3])
    can.drawString(73.25, 360.45606426789084, wrap_activities[4])
else:
    can.drawString(73.25, 450.45606426789084, activities)

##user input conclusions
conclusion = input("give the conclusions: ")

##set max length of conclusions
if len(conclusion) > 80:
    ## declare new variable to wrap where the width of it is 80 and the wrapper wont break hypens
    wrap_conclusion = textwrap.wrap(conclusion,
                                    width=80,
                                    break_on_hyphens=False)

    ## put the wrapped text in next line using coordinate[x,y] and list[0..1......]
    can.drawString(73.25, 280.20606426789084, wrap_conclusion[0])
    can.drawString(73.25, 260.20606426789084, wrap_conclusion[1])
    can.drawString(73.25, 240.20606426789084, wrap_conclusion[2])
    can.drawString(73.25, 220.20606426789084, wrap_conclusion[3])
    can.drawString(73.25, 200.20606426789084, wrap_conclusion[4])
else:
    ## if the text is not exceed 80, draw string normally in default coordinate
    can.drawString(73.25, 280.20606426789084, conclusion)

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("main_docs/daily.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("logs/out.pdf", "wb")

## set file name
fname = input("Set your file name here leh :")

## rename the default file saved using fname variable from user input
os.rename("logs/out.pdf", "logs/{}.pdf".format(fname))
output.write(outputStream)
outputStream.close()
