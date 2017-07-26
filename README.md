# coinbase-google-sheets

Gets latest Ethereum sell price off Coinbase API, puts into Google Sheets document

This app will do an update every 60 seconds. Coinbase's API updates once every 60 seconds.

## Installation

0. Install Python
1. Install pip
2. pip install requests
3. Setup Google Sheets API access; see https://developers.google.com/sheets/api/quickstart/python

    * Note: their instructions are buggy; try doing **`pip install --force-reinstall google-api-python-client` and/or pip3 with
the same arguments to get it working**
    * Note: when troubleshooting, it's handy to do `rm
~/.credentials/sheets.googleapis.com-python-quickstart.json` to start fresh
3. Update the range_output variable in app.py to the cell(s) you'd like to
update
4. python app.py --sheet_id=YourSheetId (try python3 if that doesn't work. weirdly python3 works on my Mac but python works on my Ubuntu Linux VM)

(the sheet ID is in the URL in your docs.google.com document -- it'll be after
the /d/ and before /edit)

Example spreadsheet:

![Screenshot of Google Sheets example profit loss
tracker](spreadsheet_example.png)
