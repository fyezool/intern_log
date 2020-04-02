#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import textwrap
import os
import sys
import time

from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)
x = 73.25

day = input("Enter day: ")
can.drawString(100, 630.2060642678908, day)

date = input("Enter Date: ")
can.drawString(380.64999, 630.2060642678908, date)


# Function call for writing content
def write(content, y):
    if len(content) > 80:
        y_diff = 0
        # If the text is longer than 80 characters, wrap the texts
        wrap_content = textwrap.wrap(content,
                                     width=80,
                                     break_on_hyphens=False)

        for i in wrap_content:
            # Print each line with 20 pixels difference in y-coord
            can.drawString(x, y-y_diff, i)
            y_diff += 20

    else:
        can.drawString(x, y, content)


# Getting user input
description = input("Describe what did you do today: ")
activities = input("What is the activities / work produced: ")
conclusion = input("Give the conclusion / outcome: ")


# Write the input to the canvas, and save it
write(description, 580.7060642678908)
write(activities, 450.45606426789084)
write(conclusion, 280.20606426789084)
can.save()


# move to the beginning of the StringIO buffer
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

# set file name
fname = input("Set your file name here leh:")

# rename the default file saved using fname variable from user input
os.rename("logs/out.pdf", "logs/{}.pdf".format(fname))
output.write(outputStream)
outputStream.close()
