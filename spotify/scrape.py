import pandas 
from bs4 import BeautifulSoup
import requests
from time import sleep
from datetime import date, timedelta
from selenium import webdriver
#spotify protection
#use only bs

url=[]
dates=[]
data=[]

#site mapping
#idk if date in url is needed ex:https://spotifycharts.com/regional/global/daily/2021-07-11
site = #request.get"https://spotifycharts.com/regional/global/daily/"+header
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
    #Need to figure out song_date-ex:https://stackoverflow.com/questions/2136267/beautiful-soup-and-extracting-a-div-and-its-contents-by-id
    #song_date=soup.find("div",{"class": "responsive-select"}).find("date").text
    #add in position
    #.split
    for tr in table.find("tbody").findAll("tr"):
        artist=tr.find("td", {"class": "chart-table-track"}).find("span").text
        title=tr.find("td", {"class": "chart-table-track"}).find("strong").text
        id=tr.find("td", {"class": "chart-table-image"}).find("a").get("href")
        streams=tr.find("td", {"class": "chart-table-streams"}).text
        position=tr.find("td", {"class": "chart-table-position"}).text
        song_date=y.split(site)[1]
        #breakdown by country
        #use list^
        #append to url^ 
        #{} for the f "string{variable(list or single)}"
        #Scrape position
        
        data.append([title, artist, song_date, position, streams, id])

#looping
#need review: https://selenium-python.readthedocs.io/getting-started.html
#needs a lot of review: https://sites.google.com/chromium.org/driver/
for pgs in site:
    driver=webdriver.Chrome(executable_path=r'C:\Users\camer\OneDrive\Documents\chromedriver')
    driver.get(pgs) 
    read_sngl=requests.get(pgs)
    sleep(5,15)
    soup=BeautifulSoup(driver.page_source, 'html.parser')
    table=soup.find("table", {"class":"chart-table"})
    scrape(pgs)
 
#commit and save
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
commit=pandas.DataFrame(data, columns= ["Title", "Artist", "Date", "Positon", "Streams", "ID"])

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
with open('yearsongs.csv', 'w') as f:
        commit.to_csv(f, header=True, index=False)