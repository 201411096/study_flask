# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io, shutil

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive']

def gdrive_getService():
    """
    Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\\IDE\\Projects\\test\\client_secret_143606875961-djrip4lmn4on9ae2luasnjj7tr7s1h2g.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service    

def gdrive_getFileList(service):
    results = service.files().\
            list(pageSize=10, fields="nextPageToken, files(id, name)").\
            execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

def gdrive_uploadFile(service, file_metadata, media, field):
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields=field).execute()
    print ('File ID: %s'% file.get('id'))
    return file

def gdrive_downloadFile(service, file_id, file_name=None, file_mode=None, file_mimetype=None):
    if file_mimetype is None:
        request = service.files().get_media(fileId=file_id)
    else:
        request = service.files().export_media(fileId=file_id, mimeType=file_mimetype)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%."% int(status.progress() * 100))
    
    # The file has been downloaded into RAM, now save it in a file
    fh.seek(0)

    if file_mode is None:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(fh, f)
    elif file_mode is 'text':
        print('text...')
        with open(file_name, 'wt', newline='\n') as f:
            f.write(fh.read().decode('utf-8'))

def main():
    # 0. get drive_service
    drive_service = gdrive_getService()

    # 1. get filelist example
    gdrive_getFileList(drive_service) # GoogleDrive FileList 확인

    # 2. upload file example
    # file_metadata = {'name': 'photo.jpg'}
    # media = MediaFileUpload('photo.jpg', mimetype='image/jpeg')
    # file = gdrive_uploadFile(drive_service, file_metadata, media, 'id')

    # 3. download file example
    # testcase_01
    file_id = '1WzEhWyVQ-nEhFb8L9W-RGsiydmXAh-XS'
    gdrive_downloadFile(drive_service, file_id, 'photo3.jpg')
    # testcase_02
    # file_id = '1UnQjzLM9uy9lQkLdg8-2PceDAO5QoZjD'
    # gdrive_downloadFile(drive_service, file_id, 'sample.txt', file_mode='text')    

if __name__ == '__main__':
    main()