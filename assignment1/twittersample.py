import urllib
import json


response = urllib.urlopen('http://search.twitter.com/search.json?q=microsoft')
tweets = json.load(response)['results']

for tweet in tweets:
  print tweet['text'].encode('utf-8')


