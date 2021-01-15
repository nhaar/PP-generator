import requests
import pandas as pd
from collections import OrderedDict
fhcb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpomgw2?var-5lyjej9l=z194rwyl').json()["data"]["runs"]
missions = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/7dgr41pk?var-789jpg3n=zqorp5pq').json()["data"]["runs"]
pr = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpomgw2?var-5lyjej9l=p125z8d1').json()["data"]["runs"]
allma = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/7dgr41pk?var-789jpg3n=013582dq').json()["data"]["runs"]
fiftystamps = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpm7m8k?var-wledwqen=0q5krrvq').json()["data"]["runs"]
hundredstamps = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpm7m8k?var-wledwqen=4lx3nngl').json()["data"]["runs"]
plany = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/jdz9j562?var-wled0w4n=jqzp5g4l').json()["data"]["runs"]
pl100 = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/jdz9j562?var-wled0w4n=zqod3jg1').json()["data"]["runs"]
jpaany = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/n2y5987k?var-789k195l=81p7erk1').json()["data"]["runs"]
jpaall = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/n2y5987k?var-789k195l=xqkropy1').json()["data"]["runs"]
thinice = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/z276484d?var-2lgz5d68=gq7n2yy1').json()["data"]["runs"]
asm = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/z276484d?var-2lgz5d68=21gj9km1').json()["data"]["runs"]
aba = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=814x2ykq').json()["data"]["runs"]
oneforty = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=z194zm4l').json()["data"]["runs"]
allsecret = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=p1252d21').json()["data"]["runs"]
bean = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/8246nxed').json()["data"]["runs"]
scapeany = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/ndx7q7o2?var-e8mmxoe8=21g2gpnl').json()["data"]["runs"]
scapeall = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/ndx7q7o2?var-e8mmxoe8=jqzx43g1').json()["data"]["runs"]
pearl = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/w20x36z2?var-ylqm1m7n=jq60xyoq').json()["data"]["runs"]
amethyst = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/w20x36z2?var-ylqm1m7n=5lmk480q').json()["data"]["runs"]

categories = {"fhcb": fhcb, "missions": missions, "pr": pr,"allma":allma,"fiftystamps":fiftystamps,"hundredstamps":hundredstamps,"plany":plany,"jpaany":jpaany,"jpaall":jpaall,"thinice":thinice,"asm":asm,"aba":aba,"oneforty":oneforty,"allsecret":allsecret,"bean":bean,"scapeany":scapeany,"scapeall":scapeall,"pearl":pearl,"amethyst":amethyst}
categorymaster = {}
for x in categories:
 ph = {}
 for y in range(len(categories[x])):
  try:
   ph.update({categories[x][y]["run"]["players"][0]["id"]:categories[x][y]["place"]})
  except:
   ph.update({categories[x][y]["run"]["players"][0]["name"]:categories[x][y]["place"]})
  categorymaster.update({x: ph})

points = [100,100,100,90,70,50,30,10,9,8,7,6,5,4,3,2,1]
def PP(a,b):
 i = 0
 if b>17:
  for x in range(a-1, 17):
   i += points[x]
  return i
 else:
  for x in range(a-1, b):
   i += points[x]
  return i
  
def PP_Total(e):
 pp = 0
 for x in categorymaster:
  if e in categorymaster[x]:
   pp += PP(categorymaster[x][e],len(categorymaster[x]))
  else:
   pp = pp
 return pp
 
players = []
for x in categorymaster:
 for y in categorymaster[x]:
  players.append(y)

master = {}
for x in players:
 try:
  master.update({requests.get('https://www.speedrun.com/api/v1/users/' + x).json()['data']['names']['international']: PP_Total(x)})
 except:
  master.update({x: PP_Total(x)})

newmaster = {key: value for key, value in sorted(master.items(), key=lambda item: item[1])}
finalmaster = OrderedDict(reversed(list(newmaster.items())))
with open('PP.csv', 'w') as f:
    for key in finalmaster.keys():
        f.write("%s,%s\n"%(key,finalmaster[key]))
# Bonus function: use it to get the maximum possible PP
def maxPP():
 ppmax = 0
 for x in categorymaster:
  ppmax += PP(1,len(categorymaster[x]))
 return ppmax
