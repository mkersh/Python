'''
    This script will attempt to open your webbrowser,
    perform OAuth 2 authentication and print your access token.

    It depends on two libraries: oauth2client and gflags.

    To install dependencies from PyPI:

    $ pip install python-gflags oauth2client

    Then run this script:

    $ python get_oauth2_token.py
    
    This is a combination of snippets from:
    https://developers.google.com/api-client-library/python/guide/aaa_oauth
'''

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow, argparser
from oauth2client.file import Storage

CLIENT_ID = '761551229705-9kbvia9s1s38s4dfnaa406nae04i0pt5.apps.googleusercontent.com'
CLIENT_SECRET = 'azCHp3ZTs6yTUTIfG-MiqoDc'


flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                           client_secret=CLIENT_SECRET,
                           scope='https://spreadsheets.google.com/feeds https://docs.google.com/feeds',
                           redirect_uri='http://example.com/auth_return')

storage = Storage('creds.data')

#credentials = run(flow, storage)
credentials = run_flow(flow, storage, argparser.parse_args([]))

print "access_token: %s" % credentials.access_token