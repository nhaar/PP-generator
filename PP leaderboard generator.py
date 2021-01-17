# Takes me about 90 seconds to run the script
import requests
from collections import OrderedDict

# By default this generates based on how
# the leaderboards are currently displayed.
# You can choose a specific day by changing
# x according to the following format:
# x = &date=YYYY-MM-DD
# eg.
# For runs done in October 24th 2018
# x = &date=2018-10-24

x = ''
if x:
 global y
 y = '?'+x
else:
 y = x

fhcb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpomgw2?var-5lyjej9l=z194rwyl'+x).json()["data"]["runs"]
missions = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/7dgr41pk?var-789jpg3n=zqorp5pq'+x).json()["data"]["runs"]
pr = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpomgw2?var-5lyjej9l=p125z8d1'+x).json()["data"]["runs"]
allma = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/7dgr41pk?var-789jpg3n=013582dq'+x).json()["data"]["runs"]
fiftystamps = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpm7m8k?var-wledwqen=0q5krrvq'+x).json()["data"]["runs"]
hundredstamps = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpm7m8k?var-wledwqen=4lx3nngl'+x).json()["data"]["runs"]
plany = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/jdz9j562?var-wled0w4n=jqzp5g4l'+x).json()["data"]["runs"]
pl100 = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/jdz9j562?var-wled0w4n=zqod3jg1'+x).json()["data"]["runs"]
jpaany = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/n2y5987k?var-789k195l=81p7erk1'+x).json()["data"]["runs"]
jpaall = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/n2y5987k?var-789k195l=xqkropy1'+x).json()["data"]["runs"]
thinice = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/z276484d?var-2lgz5d68=gq7n2yy1'+x).json()["data"]["runs"]
asm = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/z276484d?var-2lgz5d68=21gj9km1'+x).json()["data"]["runs"]
aba = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=814x2ykq'+x).json()["data"]["runs"]
oneforty = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=z194zm4l'+x).json()["data"]["runs"]
allsecret = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=p1252d21'+x).json()["data"]["runs"]
bean = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/8246nxed'+y).json()["data"]["runs"]
scapeany = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/ndx7q7o2?var-e8mmxoe8=21g2gpnl'+x).json()["data"]["runs"]
scapeall = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/ndx7q7o2?var-e8mmxoe8=jqzx43g1'+x).json()["data"]["runs"]
pearl = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/w20x36z2?var-ylqm1m7n=jq60xyoq'+x).json()["data"]["runs"]
amethyst = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/w20x36z2?var-ylqm1m7n=5lmk480q'+x).json()["data"]["runs"]

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
 
playersdup = []
for x in categorymaster:
 for y in categorymaster[x]:
  playersdup.append(y)

players = list(dict.fromkeys(playersdup))

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
