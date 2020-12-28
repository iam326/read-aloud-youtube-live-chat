#!/usr/bin/env python3

import boto3
import pygame.mixer
import urllib.parse
from contextlib import closing
from time import sleep

from youtube_data_api_client import YoutubeDataApiClient

YOUTUBE_DATA_CLIENT_SECRETS_FILE = "client_secrets.json"
YOUTUBE_DATA_API_CLIENT_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly']

polly = boto3.client('polly', 'ap-northeast-1')
pygame.mixer.init()


def convert_to_voice(text, path):
    result = polly.synthesize_speech(Text=text, OutputFormat='mp3',
                                     VoiceId='Joanna', Engine='neural')
    with closing(result["AudioStream"]) as stream:
        with open(path, 'wb') as file:
            file.write(stream.read())


def play_sound(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(1)
    while pygame.mixer.music.get_busy():
        sleep(0.1)


def main():
    youtube = YoutubeDataApiClient(
        YOUTUBE_DATA_CLIENT_SECRETS_FILE, YOUTUBE_DATA_API_CLIENT_SCOPES)

    url = input('YouTube Live URL: ')
    live_id = urllib.parse.urlparse(url).path[1:]
    live_chat_id = youtube.get_live_chat_id(live_id)

    next_page_token = None

    try:
        while True:
            print('get live chat messages ...')
            live_chat_messages = youtube.get_live_chat_messages(
                live_chat_id, next_page_token)

            for message in live_chat_messages['messages']:
                print(message)
                convert_to_voice(message, 'voice.mp3')
                play_sound('voice.mp3')
                sleep(1)

            next_page_token = live_chat_messages['next_page_token']
            sleep(10)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
