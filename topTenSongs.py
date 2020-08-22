import requests
from secrets import apiKey
'''rerunning the code adds api calls
so I made it an infinite loop to minimize the number of calls
you can enter in as many artists as you want without adding 
more than one call to the api!'''
url = "https://genius.p.rapidapi.com/search"

while True:
  artist = raw_input("Enter Artist Name: ")
  querystring = {"q": str(artist)}

  headers = {
      'x-rapidapi-host': "genius.p.rapidapi.com",
      'x-rapidapi-key': apiKey
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  r = response.json()

  for i in range(0,9):
    print(r['response']['hits'][i]['result']['title'])
  print ("\n")
