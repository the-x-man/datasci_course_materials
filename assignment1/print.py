import urllib
import json

url = 'http://search.twitter.com/search.json?'

def fetchTweets(page, searchKey):
  tweets = json.load(urllib.urlopen(url +'q='+searchKey +'&page='+str(page)))['results']
  return [tweet['text'].encode('utf-8') for tweet in tweets]


for page in range(1,3):
    for tweet in fetchTweets(page, 'microsoft'):
        print tweet    


