# coinbase-google-sheets
Grabs latest Ethereum sell price off Coinbase, puts into a Google Sheets document

## Installation

0. Install Python 3.x
1. Install pip
2. pip install requests
3. Setup Google Sheets API access; see https://developers.google.com/sheets/api/quickstart/python

    * Note: their instructions are buggy; try doing `pip install --force-reinstall google-api-python-client` and/or pip3 with
the same arguments to get it working
    * Note: when troubleshooting, it's handy to do `rm
~/.credentials/sheets.googleapis.com-python-quickstart.json` to start fresh

4. python3 app.py

![Screenshot of Google Sheets example profit loss
tracker](spreadsheet_example.png)
