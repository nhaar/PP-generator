import requests
import pandas as pd
fhcb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpomgw2?var-5lyjej9l=z194rwyl').json()["data"]["runs"]
missionsb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/7dgr41pk?var-789jpg3n=zqorp5pq').json()["data"]["runs"]
prb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpomgw2?var-5lyjej9l=p125z8d1').json()["data"]["runs"]
allmab = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/7dgr41pk?var-789jpg3n=013582dq').json()["data"]["runs"]
fiftystampsb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpm7m8k?var-wledwqen=0q5krrvq').json()["data"]["runs"]
hundredstampsb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/wkpm7m8k?var-wledwqen=4lx3nngl').json()["data"]["runs"]
planyb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/jdz9j562?var-wled0w4n=jqzp5g4l').json()["data"]["runs"]
pl100b = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/jdz9j562?var-wled0w4n=zqod3jg1').json()["data"]["runs"]
jpaanyb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/n2y5987k?var-789k195l=81p7erk1').json()["data"]["runs"]
jpaallb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/n2y5987k?var-789k195l=xqkropy1').json()["data"]["runs"]
thiniceb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/z276484d?var-2lgz5d68=gq7n2yy1').json()["data"]["runs"]
asmb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/z276484d?var-2lgz5d68=21gj9km1').json()["data"]["runs"]
abab = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=814x2ykq').json()["data"]["runs"]
onefortyb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=z194zm4l').json()["data"]["runs"]
allsecretb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/mkezxejk?var-789kdzql=p1252d21').json()["data"]["runs"]
beanb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/8246nxed').json()["data"]["runs"]
scapeanyb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/ndx7q7o2?var-e8mmxoe8=21g2gpnl').json()["data"]["runs"]
scapeallb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/ndx7q7o2?var-e8mmxoe8=jqzx43g1').json()["data"]["runs"]
pearlb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/w20x36z2?var-ylqm1m7n=jq60xyoq').json()["data"]["runs"]
amethystb = requests.get('https://www.speedrun.com/api/v1/leaderboards/k6q44pmd/category/w20x36z2?var-ylqm1m7n=5lmk480q').json()["data"]["runs"]

# l_i and l_(i+1) are respectively places in category and players. i are given below and are only odd values
# 1 = 500 Coins NP+
# 3 = All Missions
# 5 = 500 Coins NP
# 7 = All Missions + Awards
# 9 = 50 Stamps
# 11 = 100 Stamps
# 13 = Puffle Launch Any%
# 15 = Puffle Launch 100%
# 17 = Jet Pack Adventure Any%
# 19 = JPA All Cans 1 ups
# 21 = Thin Ice any%
# 23 = ASM
# 25 = Astro Barrier any%
# 27 = Astro Barrier 1-40
# 29 = All Secret Levels
# 31 = Bean Counters
# 33 = Pufflescape Any%
# 35 = Pufflescape 100%
# 37 = Pearl
# 39 = Amethyst
l_1 = []
l_2 = []
l3 = []
l_4 = []
l_5 = []
l_6 = []
l_7 = []
l_8 = []
l_9 = []
l_10 = []
l_11 = []
l_12 = []
l_13 = []
l_14 = []
l_15 = []
l_16 = []
l_17 = []
l_18 = []
l_19 = []
l_20 = []
l_21 = []
l_22 = []
l_23 = []
l_24 = []
l_25 = []
l_26 = []
l_27 = []
l_28 = []
l_29 = []
l_30 = []
l_31 = []
l_32 = []
l_33 = []
l_34 = []
l_35 = []
l_36 = []
l_37 = []
l_38 = []
l_39 = []
l_40 = []

for x in range(len(fhcb)):
 l_1.append(fhcb[x]["place"])
 l_2.append(fhcb[x]["run"]["players"][0]["id"])

for x in range(len(missionsb)):
 l3.append(missionsb[x]["place"])
for x in range(len(missionsb)):
 l_4.append(missionsb[x]["run"]["players"][0]["id"])

for x in range(len(prb)):
 l_5.append(prb[x]["place"])
 l_6.append(prb[x]["run"]["players"][0]["id"])
 
for x in range(len(allmab)):
 l_7.append(allmab[x]["place"])
 l_8.append(allmab[x]["run"]["players"][0]["id"])
 
for x in range(len(fiftystampsb)):
 l_9.append(fiftystampsb[x]["place"])
 l_10.append(fiftystampsb[x]["run"]["players"][0]["id"])
 
for x in range(len(hundredstampsb)):
 l_11.append(hundredstampsb[x]["place"])
 l_12.append(hundredstampsb[x]["run"]["players"][0]["id"])
 
for x in range(len(planyb)):
 l_13.append(planyb[x]["place"])
 l_14.append(planyb[x]["run"]["players"][0]["id"])
 
for x in range(len(pl100b)):
 l_15.append(pl100b[x]["place"])
 l_16.append(pl100b[x]["run"]["players"][0]["id"])
 
for x in range(len(jpaanyb)):
 l_17.append(jpaanyb[x]["place"])
 l_18.append(jpaanyb[x]["run"]["players"][0]["id"])
 
for x in range(len(jpaallb)):
 l_19.append(jpaallb[x]["place"])
 l_20.append(jpaallb[x]["run"]["players"][0]["id"])
 
for x in range(len(thiniceb)):
 if x != 7:
  l_21.append(thiniceb[x]["place"])
  l_22.append(thiniceb[x]["run"]["players"][0]["id"])
 
for x in range(len(asmb)):
 l_23.append(asmb[x]["place"])
 l_24.append(asmb[x]["run"]["players"][0]["id"])
 
for x in range(len(abab)):
 l_25.append(abab[x]["place"])
 l_26.append(abab[x]["run"]["players"][0]["id"])
 
for x in range(len(onefortyb)):
 l_27.append(onefortyb[x]["place"])
 l_28.append(onefortyb[x]["run"]["players"][0]["id"])
 
for x in range(len(allsecretb)):
 l_29.append(allsecretb[x]["place"])
 l_30.append(allsecretb[x]["run"]["players"][0]["id"])
 
for x in range(len(beanb)):
 l_31.append(beanb[x]["place"])
 l_32.append(beanb[x]["run"]["players"][0]["id"])
 
for x in range(len(scapeanyb)):
 if x != 3:
  l_33.append(scapeanyb[x]["place"])
  l_34.append(scapeanyb[x]["run"]["players"][0]["id"])
 
for x in range(len(scapeallb)):
 l_35.append(scapeallb[x]["place"])
 l_36.append(scapeallb[x]["run"]["players"][0]["id"])
 
for x in range(len(pearlb)):
 l_37.append(pearlb[x]["place"])
 l_38.append(pearlb[x]["run"]["players"][0]["id"])
 
for x in range(len(amethystb)):
 l_39.append(amethystb[x]["place"])
 l_40.append(amethystb[x]["run"]["players"][0]["id"])


fivehundred_coins_NPP = {}
for key in l_2:
   for value in l_1:
      fivehundred_coins_NPP[key] = value
      l_1.remove(value)
      break

allmissions = {}
for key in l_4:
   for value in l3:
      allmissions[key] = value
      l3.remove(value)
      break

fivehpr = {}
for key in l_6:
   for value in l_5:
      fivehpr[key] = value
      l_5.remove(value)
      break
      
allma = {}
for key in l_8:
   for value in l_7:
      allma[key] = value
      l_7.remove(value)
      break
      
fiftystamps = {}
for key in l_10:
   for value in l_9:
      fiftystamps[key] = value
      l_9.remove(value)
      break

hundredstamps = {}
for key in l_12:
   for value in l_11:
      hundredstamps[key] = value
      l_11.remove(value)
      break

plany = {}
for key in l_14:
   for value in l_13:
      plany[key] = value
      l_13.remove(value)
      break

pl100 = {}
for key in l_16:
   for value in l_15:
      pl100[key] = value
      l_15.remove(value)
      break

jpaany = {}
for key in l_18:
   for value in l_17:
      jpaany[key] = value
      l_17.remove(value)
      break

jpaall = {}
for key in l_20:
   for value in l_19:
      jpaall[key] = value
      l_19.remove(value)
      break

thinice = {}
for key in l_22:
   for value in l_21:
      thinice[key] = value
      l_21.remove(value)
      break

asm = {}
for key in l_24:
   for value in l_23:
      asm[key] = value
      l_23.remove(value)
      break

aba = {}
for key in l_26:
   for value in l_25:
      aba[key] = value
      l_25.remove(value)
      break

oneforty = {}
for key in l_28:
   for value in l_27:
      oneforty[key] = value
      l_27.remove(value)
      break

allsecret = {}
for key in l_30:
   for value in l_29:
      allsecret[key] = value
      l_29.remove(value)
      break

bean = {}
for key in l_32:
   for value in l_31:
      bean[key] = value
      l_31.remove(value)
      break

scapeany = {}
for key in l_34:
   for value in l_33:
      scapeany[key] = value
      l_33.remove(value)
      break

scapeall = {}
for key in l_36:
   for value in l_35:
      scapeall[key] = value
      l_35.remove(value)
      break

pearl = {}
for key in l_38:
   for value in l_37:
      pearl[key] = value
      l_37.remove(value)
      break

amethyst = {}
for key in l_40:
   for value in l_39:
      amethyst[key] = value
      l_39.remove(value)
      break


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

players = l_2+l_4+l_6+l_8+l_10+l_12+l_14+l_16+l_18+l_20+l_22+l_24+l_26+l_28+l_30+l_32+l_34+l_36+l_38+l_40


def PP_fhcnpp(e):
 pp = 0
 if e in fivehundred_coins_NPP:
  a = fivehundred_coins_NPP[e]
  b = len(fhcb)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_allmissions(e):
 pp = 0
 if e in allmissions:
  a = allmissions[e]
  b = len(allmissions)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_pr(e):
 pp = 0
 if e in fivehpr:
  a = fivehpr[e]
  b = len(fivehpr)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_allma(e):
 pp = 0
 if e in allma:
  a = allma[e]
  b = len(allma)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_fiftystamps(e):
 pp = 0
 if e in fiftystamps:
  a = fiftystamps[e]
  b = len(fiftystamps)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_hundredstamps(e):
 pp = 0
 if e in hundredstamps:
  a = hundredstamps[e]
  b = len(hundredstamps)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_plany(e):
 pp = 0
 if e in plany:
  a = plany[e]
  b = len(plany)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_pl100(e):
 pp = 0
 if e in pl100:
  a = pl100[e]
  b = len(pl100)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_jpaany(e):
 pp = 0
 if e in jpaany:
  a = jpaany[e]
  b = len(jpaany)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_jpaall(e):
 pp = 0
 if e in jpaall:
  a = jpaall[e]
  b = len(jpaall)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_thinice(e):
 pp = 0
 if e in thinice:
  a = thinice[e]
  b = len(thinice)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_asm(e):
 pp = 0
 if e in asm:
  a = asm[e]
  b = len(asm)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_aba(e):
 pp = 0
 if e in aba:
  a = aba[e]
  b = len(aba)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_oneforty(e):
 pp = 0
 if e in oneforty:
  a = oneforty[e]
  b = len(oneforty)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_allsecret(e):
 pp = 0
 if e in allsecret:
  a = allsecret[e]
  b = len(allsecret)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_bean(e):
 pp = 0
 if e in bean:
  a = bean[e]
  b = len(bean)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_scapeany(e):
 pp = 0
 if e in scapeany:
  a = scapeany[e]
  b = len(scapeany)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_scapeall(e):
 pp = 0
 if e in scapeall:
  a = scapeall[e]
  b = len(scapeall)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_pearl(e):
 pp = 0
 if e in pearl:
  a = pearl[e]
  b = len(pearl)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def PP_amethyst(e):
 pp = 0
 if e in amethyst:
  a = amethyst[e]
  b = len(amethyst)
  y = PP(a,b)
  pp += y 
  return pp
 else:
   pp = 0
   return pp

def Total_PP(e):
 pp = PP_fhcnpp(e)+PP_allmissions(e)+PP_pr(e)+PP_allma(e)+PP_fiftystamps(e)+PP_hundredstamps(e)+PP_plany(e)+PP_pl100(e)+PP_jpaany(e)+PP_jpaall(e)+PP_thinice(e)+PP_asm(e)+PP_aba(e)+PP_oneforty(e)+PP_allsecret(e)+PP_bean(e)+PP_scapeany(e)+PP_scapeall(e)+PP_pearl(e)+PP_amethyst(e)
 return pp

master = {}
for x in players:
 master.update({requests.get('https://www.speedrun.com/api/v1/users/' + x).json()['data']['names']['international']: Total_PP(x)})

newmaster = {key: value for key, value in sorted(master.items(), key=lambda item: item[1])}
finalmaster = OrderedDict(reversed(list(newmaster.items())))
with open('PP.csv', 'w') as f:
    for key in finalmaster.keys():
        f.write("%s,%s\n"%(key,finalmaster[key]))