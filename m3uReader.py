import urllib.request
from time import strftime
from errorMessages import mainErrors
import m3u8


def getContent(url):
    setHeader = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) xxx.net/pirdaTV' }
    sourceRequest = urllib.request.Request(url, headers=setHeader)

    try:
        response = urllib.request.urlopen(sourceRequest).read()
        return response
    except:
        timeSet = strftime("\n%Y-%m-%d %H:%M:%S", gmtime())
        print(url + timeSet + mainErrors['streamDataNotFound'])

def parseStreamingLinks(data):
    count = 0
    for i in data:
        if i == 1:
            break
        playlist = m3u8.load(i)
        print(playlist.dumps())
        count += 1

def readPlaylist():
    f = open('playlists/playlist.m3u8','r')
    fdata = f.readlines()
    f.close()
    return fdata




