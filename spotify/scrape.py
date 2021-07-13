import pandas 
from bs4 import BeautifulSoup
import requests
from time import sleep
from datetime import date, timedelta
from selenium import webdriver

url=[]
dates=[]
final=[]

#site mapping
#idk if date in url is needed ex:https://spotifycharts.com/regional/global/daily/2021-07-11
site = "https://spotifycharts.com/regional/global/daily/"
first= date(2020, 7, 11)
last= date(2021, 7, 11)
year= last-first

#needed to look up how to use timedelta: https://docs.python.org/3/library/datetime.html
for i in range(year.days+1):
	day=first+timedelta(days=i)
    #needed to look line 21 up
	day_string=day.strftime("%Y-%m-%d")
	dates.append(day_string)

#think i need this if url doesn't have dates
def add_site():
	for date in dates:
		str=site+date
		url.append(str)

add_site()

#song info
def scrape(y):
    sngl=y
    for tr in table.find("tbody").findAll("tr"):
        artist= tr.find("td", {"class": "chart-table-track"}).find("span").text
        artist= artist.replace("by ","").strip()
        title= tr.find("td", {"class": "chart-table-track"}).find("strong").text
        id= tr.find("td", {"class": "chart-table-image"}).find("a").get("href")
        id= id.split("track/")[1]
        song_date= y.split("daily/")[1]
        
        final.append([title, artist, id, song_date])

#looping
#need review: https://selenium-python.readthedocs.io/getting-started.html
for pgs in site:
    driver=webdriver.Chrome()
    driver.get(pgs) 
    read_sngl=requests.get(pgs)
    sleep(5,15)
    soup=BeautifulSoup(driver.page_source, 'html.parser')
    table=soup.find("table", {"class":"chart-table"})
    scrape(pgs)
 
#commit and save
commit = pandas.DataFrame(final, columns= ["Title", "Artist", "Song ID", "Date"])

with open('yearsongs.csv', 'w') as f:
        commit.to_csv(f, header= True, index=False)