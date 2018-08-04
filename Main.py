from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re

req = Request('http://www.espn.com/nba/teams', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

team_links = soup.find_all('a', {'href': re.compile('http://www.espn.com/nba/team/_/name/')})
f = open("roster.txt", 'w')
for link in team_links:
    link = link['href']
    link = link[0:29] + 'roster/_' + link[30:]
    f.write('#'+link.rsplit('/',1)[1].replace('-',' ').title()+'\n')
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    count = 0
    for item in soup.find("table", {"class": "tablehead"}).children:
        count += 1
        if count > 2:
            f.write(item.get_text(" ").replace(u'\xa0', u' ')+'\n')