from __future__ import print_function
import datetime
import httplib2
import os
import time
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import requests


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'sheets.googleapis.com-'
                                   'python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_eth_usd_sell_price():
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/sell'
    response = requests.get(url)
    json = response.json()
    return str(json['data']['amount'])


def main():
    """ Every 60 seconds updates a Google Sheets spreadsheet with current
    timestamp and latest Ethereum coin sell price from Coinbase
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = 'just-an-example ... update-this'
    while True:
        timestamp = str(datetime.datetime.now())
        price = get_eth_usd_sell_price()
        print(timestamp, price)
        myBody = {u'range': u'Sheet1!C1:C2', u'values': [[timestamp],
                  [price]]}
        rangeOutput = 'Sheet1!C1:C2'
        res = service.spreadsheets().values().update(
            spreadsheetId=spreadsheetId, range=rangeOutput,
            valueInputOption='RAW', body=myBody).execute()
        time.sleep(10)


if __name__ == '__main__':
    main()
