"""
To get this working in python 3 (as well as 2) I had to download latest PyDrive from:
https://github.com/googledrive/PyDrive.git
and do a manual python setup install.
"""
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from apiclient import errors

def insert_file_into_folder(service, folder_id, file_id):
  """Insert a file into a folder.

  Args:
    service: Drive API service instance.
    folder_id: ID of the folder to insert the file into.
    file_id: ID of the file to insert.
  Returns:
    The inserted parent if successful, None otherwise.
  """
  new_parent = {'id': folder_id}
  try:
    return service.parents().insert(
        fileId=file_id, body=new_parent).execute()
  except errors.HttpError as error:
    print('An error occurred: %s' % error)
  return None

def download_file(service, drive_file):
  """Download a file's content.

  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
  """
  download_url = drive_file.get('downloadUrl')
  if download_url:
    resp, content = service._http.request(download_url)
    if resp.status == 200:
      print('Status: %s' % resp)
      return content
    else:
      print('An error occurred: %s' % resp)
      return None
  else:
    # The file doesn't have any content stored on Drive.
    #download_url = drive_file['exportLinks']['application/pdf']
    download_url = drive_file['exportLinks']['text/html']
    resp, content = service._http.request(download_url)
    return content

def main():
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication

  drive = GoogleDrive(gauth)

  # Find a root level folder called TestFolder3
  file_list = drive.ListFile({'q': "'root' in parents and title='TestFolder3'"}).GetList()
  print("Searching for TestFolder3 returned {0} items. {1}".format(len(file_list),file_list[0]['id']))
  dirId = file_list[0]['id']

  fileQueryStr = "'{0}' in parents and trashed=false".format(dirId)
  # Auto-iterate through all files that matches this query
  #file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
  file_list = drive.ListFile({'q': fileQueryStr}).GetList()
  for file1 in file_list:
    try:
    	print('title: %s, id: %s\nContents:%s\n' % (file1['title'], file1['id'], file1.GetContentString() ))
    except Exception as e:
    	print("Can not get contents of {0}{1}".format(file1['title'], file1['mimeType']))
      # Next lines show how you can get the content of a google doc file
    	#service = gauth.service
    	#print(download_file(service,file1))
  # Create a new file
  file1 = drive.CreateFile({'title': 'Hello.txt'}) # Create GoogleDriveFile instance with title 'Hello.txt'
  file1.SetContentString('Hello World!') # Set content of the file from given string
  file1.Upload() # Upload it

  # This next line show getting hold of the google service obj from the auth object
  insert_file_into_folder(gauth.service, dirId, file1['id'])
  print('Created new file: %s, id: %s' % (file1['title'], file1['id'])) # title: Hello.txt, id: {{FILE_ID}}

  # If you don't force exit you get a load of shutdown errors in python 3
  sys.exit(0)

if __name__ == '__main__':
  main()