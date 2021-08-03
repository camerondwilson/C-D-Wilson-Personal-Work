import pandas 
from bs4 import BeautifulSoup
import requests
from time import sleep
from datetime import date, timedelta
#spotify protection
#use only bs

url=[]
dates=[]
data=[]

country="global"
#site mapping
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
site = f"https://spotifycharts.com/regional/{country}/daily/"
first= date(2021, 1, 1)
last= date(2021, 7, 17)
year= last-first

#needed to look up how to use timedelta: https://docs.python.org/3/library/datetime.html
for i in range(year.days+1):
	day=first+timedelta(days=i)
    #needed to look line 21 up
	day_string=day.strftime("%Y-%m-%d")
	dates.append(day_string)

def add_site():
	for date in dates:
		str=site+date
		url.append(str)

add_site()

#song info
def scrape(y):
    sngl=y

    for tr in table.find("tbody").findAll("tr"):
        artist=tr.find("td", {"class": "chart-table-track"}).find("span").text

        title=tr.find("td", {"class": "chart-table-track"}).find("strong").text

        id=tr.find("td", {"class": "chart-table-image"}).find("a").get("href")
        id=id.split("track/")[1]

        streams=tr.find("td", {"class": "chart-table-streams"}).text

        position=tr.find("td", {"class": "chart-table-position"}).text

        song_date=y.split(site)[1]

        country=list.append('https://spotifycharts.com/regional/' + country + '/daily/' + song_date.strftime("%Y-%m-%d"))
        #breakdown by country
        #use list^
        #append to url^ 
        #{} for the f "string{variable(list or single)}"
        
        data.append([title, artist, song_date, position, streams, id, country])

#looping
#need review: https://selenium-python.readthedocs.io/getting-started.html
#needs a lot of review: https://sites.google.com/chromium.org/driver/
for u in site:
    read=requests.get(u, headers=headers)
    sleep(2)
    soup=BeautifulSoup(read.text, "html.parser")
    table=soup.find("table", {"class":"chart-table"})
    scrape(u)
 
#commit and save
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
commit=pandas.DataFrame(data, columns= ["Title", "Artist", "Date", "Positon", "Streams", "ID", "Country"])

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
with open('yearsongs.csv', 'w') as f:
        commit.to_csv(f, header=True, index=False)