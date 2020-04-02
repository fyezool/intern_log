## Daily & Weekly Log for UCTS internship

### This Project Basically :- 

1. Automate the logbook using pdf, reportlab, pypdf2
2. Honing Python skill for Nton Smart Inventory project
3. Utilize free time during Movement Control Order (MCO) happening in Malaysia
4. Inspired by a [classmate's](https://github.com/tyu1996) post on automation, hence, tried myself for the sake of curiosity

### Pre-requisites
1. Main program requires following modules to run: pypdf2, reportlab
2. Miner requires pdfminer modules to run

### Use It for the Sake of Automation(Fancy Word for Lazy)
1. Run daily_log.py
2. Enter **day**, **date**, **activities**, **work produced**, **comments on the activities** and give **name** for your file.
3. Produced logs will be on **__logs__** folder. 
4. Print that thing.

### How Does It Works

1. Pdf file **__daily__** and **__weekly__** scraped using **__miner_daily__** and **__miner_weekly__** to get the position of textfield instead of blind guess
2. Modify the coordinate a bit just to make sure it is accurate
3. **__daily_log.py__** then will copy all **__daily.pdf__** content then insert all input data from user then create new file according to the user


### Achieving Text Wrapping
1. Use _if_ to decide max length for a line of text
2. Use Python's textwrap method ```textwrap.wrap(content, width=80, break_on_hyphens=False)``` and store it as a new list
3. Display stored text using _for_ loop, for each line of text being displayed with y-coordinate offsets
4. Profit
5. Best of luck on your internship guys.


### References
1. [Main code](https://stackoverflow.com/questions/6819336/add-text-to-existing-pdf-document-in-python)
2. [Pdf scraping 101](https://pdfminer-docs.readthedocs.io/programming.html#performing-layout-analysis)
3. [Another pdf scraping](https://towardsdatascience.com/web-scraping-101-in-python-35f8653b1c97)
4. [Text wrapping](https://stackoverflow.com/questions/41553666/reportlab-wrap-with-drawstring)

### TODO
- Fetch file from specific folder then use cron to execute python script
- Input error control
- Modularise the program
- You tell?
