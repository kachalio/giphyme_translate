import requests
import json
import sys
import webbrowser

GIPHYHOST = 'http://api.giphy.com'
GIPHYKEY = '&api_key=dc6zaTOxFJmzC'
GROUPME_BOT_ID = 'Your Bot ID  Here'  ## Need to add Bot ID ##
GROUPME_BOT_POST = 'https://api.groupme.com/v3/bots/post'

def giphySearch(search):
	translategif = requests.get(GIPHYHOST + '/v1/gifs/translate?s=' + search + GIPHYKEY)
	result = translategif.json()
	#selects the raw gif url.  urls for other sizes are available in the json
	rawGIF = result['data']['images']['original']['url']
	return rawGIF

def groupmePost(gif):
	#Testgroup
	data = { 'bot_id' : GROUPME_BOT_ID, 'text': gif}
	r =  requests.post(GROUPME_BOT_POST, data=data)

def main():
	#Parses text sent from the PHP script and builds search string
	search = ''
	for x in range(1,len(sys.argv)):
		search = search + sys.argv[x] + ' '
	
	#search string passed to giphy API
	gif_url = giphySearch(search)
	
	#gif passed to groupme API
	groupmePost(gif_url)

if __name__ == '__main__':
	main()











