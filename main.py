import http.client
import json
import requests
conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "8b527124320dc31cc39829d33e8b1390"
    }

conn.request("GET", "/transfers?player=35845", headers=headers)

res = conn.getresponse()
data = res.read()
jsonData = json.loads(data)
responses = jsonData['response']
for response in responses:
  playerName = response['player']['name']
  transfers = response['transfers'] 
  transfers = response['transfers']['date']
  n = len(transfers)
  lastTransfer = transfers[n-1]
  print(f"Player name is {playerName}")
  print(f"latest tranfer {lastTransfer}")
  


  
  #print(f"transfer date is {transfers}")
  #0print(f"Player tranfers are {transfers}")


