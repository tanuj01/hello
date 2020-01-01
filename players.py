# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:56:52 2019 

@author: tanuj
"""

import requests  
import bs4
import io
import lxml
import re

url="http://www.espncricinfo.com/ci/content/player/index.html"
data=requests.get(url)
#print(data.text)
#print(type(data))
data=bs4.BeautifulSoup(data.text,"lxml")
#print(type(data))
mainurl="http://www.espncricinfo.com/ci/content/player/caps.html?country="
total=data.select(".ciPlayersHomeCtryList")
#print(total)
for i in total:
    teams=i.find_all("a")
    #print(teams)

count=len(teams)
for j in range(count):
    url=teams[j].get("href")
    #print(url)
    url=re.split("=",url)
    url1=mainurl+url[1]+";class=1"
    teamdata=requests.get(url1)
    teamdata=bs4.BeautifulSoup(teamdata.text,"lxml")
    playerdata=teamdata.select(".ciPlayerbycapstable")
    with io.open(teamname +".csv","w",encoding="utf8") as f1:
        f1.write("TEAMNAME,NUMBER,NAME,DEBUTDATE \n")
        f1.close()
    print(len(playerdata))
    for k in playerdata:
        playerstats=k.find_all("l1",class_="sep")
        for m in playerstats:
            number=m.find_all("l1",class_="ciPlayerbycapstable")
            if(len(number)<1):
                number=m.find_all("l1",class_="ciPlayerserialno")
                name=m.find_all("l1",class_="ciPlayername")
                print(name[0].text)
                debutdate=m.find_all("l1",class_="ciPlayerplayed")
                print(debutdate[0].text)
                
                dataline=teamname + "," + number[0].text + "," + name[0].text + "," + debutdate[0]
                with io.open(teamname +".csv","a",encoding="utf8") as f1:
                    f1.write(dataline + "\n")
                    f1.close()
                    
print("done")
    