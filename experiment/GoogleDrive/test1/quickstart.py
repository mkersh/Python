"""
To get this working in python 3 (as well as 2) I had to download latest PyDrive from:
https://github.com/googledrive/PyDrive.git
and do a manual python setup install.
"""
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication

drive = GoogleDrive(gauth)

# Auto-iterate through all files that matches this query
#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
file_list = drive.ListFile({'q': "'0B-yS3iG3xHVuZVBfT2p3RENjYTQ' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

# If you don't force exit you get a load of shutdown errors in python 3
sys.exit(0)