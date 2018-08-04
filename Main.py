from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re

req = Request('http://www.espn.com/nba/teams', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

team_links = soup.find_all('a', {'href': re.compile('http://www.espn.com/nba/team/_/name/')})

for link in team_links:
    link = link['href']
    link = link[0:29] + 'roster/_' + link[30:]
    print(link.rsplit('/',1)[1].replace('-',' ').title())
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    #player_links = soup.find_all('a', {'href': re.compile('http://www.espn.com/nba/player/_/id/')})

    #for link2 in player_links:
        #f.write(link2.text + '\n')
    count = 0
    f = open(link.rsplit('/', 1)[1] + ".txt", 'w')
    for item in soup.find("table", {"class": "tablehead"}).children:
        count += 1
        if count > 2:
            prev = '0'
            print(item.get_text(" "))