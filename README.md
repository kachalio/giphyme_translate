# groupy_translate
Small framework that allows the Giphy translate API to be used in GroupMe.  When "/giphy" followed by some keywords are sent to the group, a random gif related to those keywords is posted by a bot.  Ex. "/giphy tiger woods" returns tiger woods related .gifs.

Giphy api info regarding translate function found here: https://api.giphy.com/
GroupMe api info found here: https://dev.groupme.com/

#Requirements: 
A server where the groupmeBot.php can live and accept post requests.
A GroupMe Bot for the group you want this to work in.  The callback url will then need to be set to the location of the .php script.  More info here: https://dev.groupme.com/tutorials/bots

#How it works
When a group member sends a message to the group, the Bot sends a POST request to your callback url (where the .php script is).  The script parses the text from the message to see if "/giphy" is included, if true, then the keywords after "/giphy" will be used to search giphy for .gifs.  That will return a .gif and post it to the groupme group.
