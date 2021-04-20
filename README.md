# Spotify Album to Notion Page

This is a code to download the album data from Spotify and store it on a Notion Page as a table.

![NotionIntroduction](https://github.com/pinnzonandres/SpotiNotion/blob/master/Img/Notion.PNG?raw=true)

## Required Packages

### Spotipy
The package Spotipy is a lightweight Python library for the [Spotify](https://spotipy.readthedocs.io/en/2.18.0/) Web API.

`pip install spotipy`

### Notion-py

Unofficial Python 3 client for Notion. I recommend go to [pypi](https://pypi.org/project/notion-py/) and download the package as tar.gz. In  folder where the file is saved, open your dash and write

`pip install notion-py-0.0.9.tar.gz`

## Get the Spotify and Notion Clients

### Spotify Client

Go to [spotify developer](https://developer.spotify.com/), go to dashboard, sign up and create and app, then get the client tokens.

![SpotifyClients](C:\Users\Pinnzon\Desktop\SpoNotion\Img\SpoDeve.png)

Then add your tokens on the code
```

client_id="<Put your developer spotify cliend id>"
client_secret= "<Put your developer spotify client_secret>"

```

