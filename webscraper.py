#setup for our webscraper
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv
driver=webdriver.Chrome()

###change below line
url = "https://results.run.tf/meets/28894"
hyperlinkArr = []
superArr = []
driver.get(url)
sleep(1.5)
#here we are finding all of the tags for a given meet page
soup = BeautifulSoup(driver.page_source, 'html.parser')
a_tags = soup.find_all('a',"events-table--row-link")
for i in a_tags:
    if i.has_attr('href'):
        #print(i['href'])
        hyperlinkArr.append(i['href'])

#now let's look at each hyperlink of those events
def eventScraper(urlIN):
    url = "https://live.usp-sports.com/" + urlIN
    driver.get(url)
    sleep(2)
    s1 = BeautifulSoup(driver.page_source, 'html.parser')
    #print(s1.prettify())
    result_tags=s1.find_all("div","results-table--row")
    eventName=s1.find_all("h3")
    print(eventName[0].text.strip())
    for i in result_tags:
        #name
        name = i.find_all('div',"results-table--grid--title results-table--ell-overflow")
        print(name[0].text.strip())
        #team name
        teamName = i.find_all("div","results-table--grid--team-name results-table--ell-overflow")
        print(teamName[0].text.strip())
        #result/time
        result = i.find_all("div","results-table--grid--title")
        print(result[1].text.strip())
        superArr.append([eventName[0].text.strip(),name[0].text.strip(),teamName[0].text.strip(),result[1].text.strip()])
for i in hyperlinkArr:
    if 'relay' in i:
        pass
    else :
        eventScraper(i)
print('done!')
with open("Bow Tie.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(superArr)