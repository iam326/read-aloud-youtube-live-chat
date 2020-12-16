#!/usr/bin/env python3

import math
import urllib.parse
from time import sleep

from youtube_data_api_client import YoutubeDataApiClient

YOUTUBE_DATA_CLIENT_SECRETS_FILE = "client_secrets.json"
YOUTUBE_DATA_API_CLIENT_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly']


def main():
    youtube = YoutubeDataApiClient(
        YOUTUBE_DATA_CLIENT_SECRETS_FILE, YOUTUBE_DATA_API_CLIENT_SCOPES)

    url = input('YouTube Live URL: ')
    live_id = urllib.parse.urlparse(url).path[1:]
    live_chat_id = youtube.get_live_chat_id(live_id)

    next_page_token = None
    while True:
        live_chat_messages = youtube.get_live_chat_messages(
            live_chat_id, next_page_token)
        next_page_token = live_chat_messages['next_page_token']
        print(live_chat_messages['messages'])
        sleep(10)


if __name__ == '__main__':
    main()
