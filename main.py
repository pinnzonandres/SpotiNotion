#Spotify Modules
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import logging
#Notion Modules
from notion.client import NotionClient
import notion
from notion.block import PageBlock
from md2notion.upload import upload

logger = logging.getLogger('examples.artist_albums')

client_id="<Put your developer spotify cliend id>"
client_secret= "<Put your developer spotify client_secret>"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_artist_albums(artist):
    albums = []
    final_albums={"Album_Name":[],"Date":[],}
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = set()  # to avoid dups
    albums.sort(key=lambda album: album['release_date'].lower())
    for album in albums:
    	name = album['name']
    	if name not in seen:
        	final_albums["Album_Name"].append(album['name'])
        	final_albums["Date"].append(album['release_date'])
        	seen.add(name)
    return final_albums

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def get_data(data):
    dicta = data
    colA = getList(dicta)
    dataA = pd.DataFrame(dicta, columns=colA)
    return dataA


client = NotionClient(token_v2="<Put your Token>")
page = client.get_block("<Put the notion page link>")

def upload_notion_data(Art,data):
    A= get_data(data)
    A.to_markdown("data.md",index = False) 
    with open("data.md","r", encoding="utf-8") as mdfile: 
        newPage = page.children.add_new(PageBlock, title=Art+" discography")
        upload(mdfile, newPage)
        print('Uploading the album data')

def main():
    print('Artist')
    Art = input()
    Artist = get_artist(Art)
    if Artist:
        data = show_artist_albums(Artist)
        upload_notion_data(Art)
    else:
        logger.error("Can't find artist: %s", Art)
    


if __name__ == '__main__':
    main()
