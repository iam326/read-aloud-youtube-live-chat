#!/usr/bin/env python3

import os

import httplib2

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the API Console
https://console.developers.google.com/
For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
"""


class YoutubeDataApiClient():

    def __init__(self, client_secrets_file, scopes):
        self.__client = self.get_youtube_data_api_client(
            client_secrets_file, scopes)

    def get_youtube_data_api_client(self, client_secrets_file, scopes):
        message = MISSING_CLIENT_SECRETS_MESSAGE % os.path.abspath(
            os.path.join(os.path.dirname(__file__), client_secrets_file))
        flow = flow_from_clientsecrets(client_secrets_file,
                                       scope=scopes,
                                       message=message)

        storage = Storage('youtube-oauth2.json')
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, storage)

        return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                     http=credentials.authorize(httplib2.Http()))

    def get_live_chat_id(self, live_id):
        live_broadcasts = self.__client.liveBroadcasts().list(
            part='snippet', id=live_id).execute()

        return live_broadcasts['items'][0]['snippet']['liveChatId']

    def get_live_chat_messages(self, live_chat_id, next_page_token=None):
        live_chat_messages = self.__client.liveChatMessages().list(
            liveChatId=live_chat_id,
            part='snippet',
            maxResults=200,
            pageToken=next_page_token
        ).execute()

        return {
            'next_page_token': live_chat_messages['nextPageToken'],
            'messages': [i['snippet']['displayMessage'] for i in live_chat_messages['items']]
        }
