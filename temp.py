import os
import json
election_search = "Joe Donnelly Mike Braun"

if(os.path.isfile('DATA-TWEETS ' + election_search + '.txt')):
	with open('DATA-TWEETS ' + election_search + '.txt','r') as fp:
		collection_of_tweets = json.load(fp)
		
print(os.path.isfile('DATA-TWEETS ' + election_search + '.txt'))

from pathlib import Path

print(Path().absolute())