# read-out-youtube-live-chat

YouTube Live のチャットを Raspberry Pi に読ませる

## Environment

```
$ cat /proc/device-tree/model
Raspberry Pi 2 Model B Rev 1.1

$ lsb_release -a
No LSB modules are available.
Distributor ID: Raspbian
Description: Raspbian GNU/Linux 10 (buster)
Release: 10
Codename: buster

$ python3 --version
Python 3.7.3

$ pip3 --version
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)

$ aws --version
aws-cli/1.18.199 Python/3.7.3 Linux/5.4.51-v7+ botocore/1.19.39
```

## Requirements

- [Python から OAuth 2.0 認証を通して YouTube Data API を叩く](https://dev.classmethod.jp/articles/oauth2-youtube-data-api/) を参考にして、OAuth 2.0 クライアントの情報を含む JSON ファイルを作成する。また、作成した JSON ファイルの名前を `client_secrets.json` に変更する

## Setup

```
$ pip3 install -r requirements.txt
```

## Usage

```
$ python3 main.py
```
