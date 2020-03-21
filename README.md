## Daily & Weekly Log for UCTS internship

### This project aim to 

- Automate the logbook using pdf, reportlab, pypdf2
- Honing Python skill for Nton SMart Inventory project
- Utilize free time during Restricted Movement Order 18-31 March
- Inspired by classmate post on automation, hence, tried myseld for the sake of curiosity

## How does it works

1. Pdf file 'daily' and 'weekly' scraped using 'miner_daily' and 'miner_weekly' to get the position of textfield instead of blind guest\
2. Modify the coordinate a bit just to make sure it is accurate
3. 'daily.py' then will copy all 'daily.pdf' content then insert all input data from user then create new file according to the user


## Text Wrapping fix
1. use if to set text max length
2. 'wrap_description = textwrap.wrap(description, width=80, break_on_hyphens=False)' set new var for wrapped text and store it
3. Display stored text using 'canvas.drawString' and list[] + new coordinate for new line of text
4. Profit
5. Best of luck on your internship guys.

