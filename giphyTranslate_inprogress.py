'''
This script is currently able to pull search post giphy translate gifs.  Group Id for the Groupme group was hardcoded however, so in the process of automating that.  I have built a function that can identify all the group ids associated with your api key.

Need to find a way to accept json from php script for the purpose of getting the group id from the message sender.  Problem is in the argument parsing, where the current parser relies on only search terms being passed as arguments to the scripts.
'''

import requests
import json
import sys
import webbrowser

########################
# Giphy Search section #
########################

#Constants
GIPHYHOST = 'http://api.giphy.com'
GIPHYKEY = '&api_key=dc6zaTOxFJmzC'
#Parses the arguments passed from server
search = ''
arglen = len(sys.argv)
jsondata = sys.argv[arglen - 1]

for x in range(1,len(sys.argv) - 1):
	search = search + sys.argv[x] + ' '
print(search)
print(jsondata)
'''
Need to make jsondata match up to groupme group id
'''
#Request to Giphy api and json result
translategif = requests.get(GIPHYHOST + '/v1/gifs/translate?s=' + search + GIPHYKEY)
print(translategif.status_code)
result = translategif.json()
#Getting raw .gif from json
rawGIF = result['data']['images']['original']['url'] #Translate
#for testing
print(rawGIF)
#webbrowser.open(rawGIF)

#Helt Texas
#data = { 'bot_id' : 'KEY', 'text': rawGIF} 
#Testgroup
#data = { 'bot_id' : 'KEY', 'text': rawGIF}
#r =  requests.post(botpost, data=data)

###################
# Groupme Section #
###################
#Constants
GROUPMEHOST = 'https://api.groupme.com/v3'
GROUPMEKEY = '?token=KEY'

#Returns list of all group id's
def getGroupIDs():
	z = requests.get(GROUPMEHOST + '/groups' + GROUPMEKEY)
	groups = z.json()
	group_list = []
	all_groups = groups['response']
	for x in range(0, len(all_groups)):
		group_list.append(all_groups[x]['group_id'])
	return group_list

group_list = getGroupIDs()
for p in group_list : print p















