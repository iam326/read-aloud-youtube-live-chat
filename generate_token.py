#!/usr/bin/env python3

from youtube_data_api_client import YoutubeDataApiClient

YOUTUBE_DATA_CLIENT_SECRETS_FILE = 'client_secrets.json'
YOUTUBE_DATA_API_CLIENT_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly']


if __name__ == '__main__':
    YoutubeDataApiClient(YOUTUBE_DATA_CLIENT_SECRETS_FILE,
                         YOUTUBE_DATA_API_CLIENT_SCOPES)
    print('done!')
