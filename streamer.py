from errorMessages import mainErrors
from time import gmtime, strftime
import urllib.request

def streamRequest(url):
    setHeader = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) prologas.net/pirdaTVparser' }
    sourceRequest = urllib.request.Request(url, headers=setHeader)

    try:
        response = urllib.request.urlopen(sourceRequest).read()
        return response
    except:
        timeSet = strftime("\n%Y-%m-%d %H:%M:%S", gmtime())
        print(url + timeSet + mainErrors['streamDataNotFound'])