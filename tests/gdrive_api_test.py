from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

import constants

# If modifying these scopes, delete the file token.pickle.

SCOPES = ['https://www.googleapis.com/auth/drive.file']


def get_gdrive_service():
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # return Google Drive API service
    return build('drive', 'v3', credentials=creds)


def upload_files():
    """
    Creates a folder and upload a file to it
    """
    # authenticate account
    service = get_gdrive_service()
    # folder details we want to make
    # folder_metadata = {
    #     "name": "Python-version",
    #     "mimeType": "application/vnd.google-apps.folder"
    # }
    # # create the folder
    # file = service.files().create(body=folder_metadata, fields="id").execute()
    # # get the folder id
    # folder_id = file.get("id")
    # print("Folder ID:", folder_id)
    # # upload a file text file
    # # first, define file metadata, such as the name and the parent folder ID
    file_metadata = {
        "name": constants.FILENAME,
        # "parents": [folder_id]
    }
    # upload
    media = MediaFileUpload(constants.FILENAME, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print("File created, id:", file.get("id"))


def main():
    service = get_gdrive_service()
    upload_files()


if __name__ == '__main__':
    main()
