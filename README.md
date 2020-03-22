## Daily & Weekly Log for UCTS internship

### This project basically :- 

1. Automate the logbook using pdf, reportlab, pypdf2
2. Honing Python skill for Nton Smart Inventory project
3. Utilize free time during Restricted Movement Order 18-31 March
4. Inspired by classmate post on automation, hence, tried myself for the sake of curiosity

### Use it for the sake of automation(fancy word for lazy)
1. Run daily_log.py
2. Enter **day**, **date**, **activities**, **work produced**, **comments on the activities** and give **name** for your file.
3. Produced logs will be on **__logs__** folder. 
4. Print that thing.

### How does it works

1. Pdf file **__daily__** and **__weekly__** scraped using **__miner_daily__** and **__miner_weekly__** to get the position of textfield instead of blind guess
2. Modify the coordinate a bit just to make sure it is accurate
3. **__daily_log.py__** then will copy all **__daily.pdf__** content then insert all input data from user then create new file according to the user


### Text Wrapping fix
1. use if to set text max length
2. ```wrap_description = textwrap.wrap(description, width=80, break_on_hyphens=False)``` set new var for wrapped text and store it
3. Display stored text using ```canvas.drawString``` and ```list[ ]``` + new coordinate for new line of text
4. Profit
5. Best of luck on your internship guys.


### References
1. [Main code](https://stackoverflow.com/questions/6819336/add-text-to-existing-pdf-document-in-python)
2. [Pdf scraping 101](https://pdfminer-docs.readthedocs.io/programming.html#performing-layout-analysis)
3. [Another pdf scraping](https://towardsdatascience.com/web-scraping-101-in-python-35f8653b1c97)
4. [Text wrapping](https://stackoverflow.com/questions/41553666/reportlab-wrap-with-drawstring)

### TODO
- Fetch file from specific folder then use cron to execute python script
- You tell?
