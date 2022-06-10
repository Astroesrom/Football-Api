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
 
  lastTransfer = transfers[0]
  transferDate= lastTransfer['date']
  currenttTeamName= lastTransfer['teams']['out']['name']
  newTeamName= lastTransfer['teams']['in']['name']
  print(f"Player name that is being tranfered is {playerName}")
  print(f"The tranfer is taking place in {transferDate}")
  print(f"The team he is currently playing for is {currenttTeamName}")
  print(f"The team that he will be transfered to is {newTeamName}")
  #print(f"latest tranfer {lastTransfer}")
  
  


 

