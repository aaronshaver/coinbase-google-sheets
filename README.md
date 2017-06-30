# coinbase-google-sheets
Grabs latest Ethereum sell price off Coinbase, puts into a Google Sheets document

## Installation

0. Setup Google Sheets API access (note, their instructions are buggy; try
doing `pip install --force-reinstall google-api-python-client` and/or pip3 with
the same arguments to get it working)
Note: when troubleshooting, it's handy to do `rm
~/.credentials/sheets.googleapis.com-python-quickstart.json` to start fresh
1. Install Python 3.x
2. Install pip
3. pip install requests
4. python3 app.py


