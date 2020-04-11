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
can.setFont("Helvetica", 12)
x = 64.14

day = input("Enter day: ")
can.drawString(96.14, 674.804, day)

date = input("Enter Date: ")
can.drawString(374.58, 674.804, date)


# Function call for writing content
def write(content, x, y):
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
weekly_report = input("Industrial Training Weekly Report: ")
student_name = input("Your name: ")


# Write the input to the canvas, and save it
write(weekly_report, x, y=622.004)
write(student_name, x=104.14, y=318.33599999999996)
write(date, x=99.14, y=288.936)
can.save()


# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("main_docs/weekly.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


# set file name
fname = input("Set your file name here leh: ")

# finally, write "output" to a real file
outputStream = open("output/weekly/{}.pdf".format(fname), "wb")
output.write(outputStream)
outputStream.close()
