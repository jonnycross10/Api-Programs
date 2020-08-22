from __future__ import print_function 
from secrets import apiKey
#overwrites print statement with print function to get rid of newlines when printing

import requests
import urllib #for encoding url input

url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer-url"

headers = {
    'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com",
    'x-rapidapi-key': apiKey,
    'content-type': "application/x-www-form-urlencoded"
    }

while True:
  article = raw_input("Enter an article's URL: ")
  sentnum = int(raw_input("How many sentences do you want the summary to be? "))
  article =  urllib.quote_plus(article)
  payload = "url=" + article + "&sentnum=" + str(sentnum)

  response = requests.request("POST", url, data=payload, headers=headers)
  r = response.json()
  print('\n')
  for i in range(0,sentnum):
    print (r["sentences"][i], end = '')
  print('\n')



