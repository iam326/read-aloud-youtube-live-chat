#!/usr/bin/env python3

import math
import urllib.parse
from contextlib import closing
from time import sleep

import boto3

from youtube_data_api_client import YoutubeDataApiClient

YOUTUBE_DATA_CLIENT_SECRETS_FILE = "client_secrets.json"
YOUTUBE_DATA_API_CLIENT_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly']

polly = boto3.client('polly')


def convert_to_voice(path, text):
    result = polly.synthesize_speech(Text=text, OutputFormat='mp3',
                                     VoiceId='Joanna', Engine='neural')
    with closing(result["AudioStream"]) as stream:
        with open(path, 'wb') as file:
            file.write(stream.read())


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

        for message in live_chat_messages['messages']:
            convert_to_voice('voice.mp3', message)
            # Raspberry PI で読ませる
            print(message)

        next_page_token = live_chat_messages['next_page_token']
        sleep(10)


if __name__ == '__main__':
    main()
