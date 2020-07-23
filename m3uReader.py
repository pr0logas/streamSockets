from defaults import sourceM3u8
import urllib.request
from time import strftime
from errorMessages import mainErrors


def getContent(url):
    setHeader = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) xxx.net/pirdaTV' }
    sourceRequest = urllib.request.Request(url, headers=setHeader)

    try:
        response = urllib.request.urlopen(sourceRequest).read()
        return response
    except:
        timeSet = strftime("\n%Y-%m-%d %H:%M:%S", gmtime())
        print(url + timeSet + mainErrors['streamDataNotFound'])

def truncateTheFile():
    f = open('playlists/playlist.m3u','a')
    f.seek(0)
    f.truncate()

def writePlaylistToFile(data):
    f = open('playlists/playlist.m3u','a')
    f.write(data)
    f.close()

def readPlaylist():
    f = open('playlists/playlist.m3u','r')
    fdata = f.readlines()
    f.close()
    return fdata

def firstAggregation(data):
    playList = []
    for line in data:
        if line != '\n':
            line2 = line.replace("\n", "")
            playList.append(line2)
    return playList

m3u8Content = getContent(sourceM3u8).decode("utf-8")
writePlaylistToFile(m3u8Content)
result = firstAggregation(readPlaylist())
truncateTheFile()

for i in result:
    if i.startswith( 'http://stream' ):
        writePlaylistToFile(i + '\n')
