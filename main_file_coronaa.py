from plyer import notification# use to give notification in windows
import requests #to get data from mhfw website
import time
from bs4 import BeautifulSoup

def notifyme(title,msg):
    notification.notify(
        title=title,
        message=msg,
        app_icon="E:\#quarntine\Corona Virus update\icon.ico",#support ico file format not png
        timeout = 15)

def getData(url):
    r=requests.get(url)
    return r.text
while True:
#notifyme("Nikita","Hows your work going?")

    myData=getData("https://www.mohfw.gov.in/")
    soup=BeautifulSoup(myData,'html.parser')
    #print(soup.prettify())
    #use bs4 to convrt web data in desired format
    myDatastr=""
    for tr in soup.find('tbody').find_all('tr'):#u will find table from the pg
        myDatastr+=tr.get_text()
    myDatastr=myDatastr[1:]
    itemlist=(myDatastr.split("\n\n"))
    states=['Maharashtra']
    for item in itemlist[0:35]:
        #print(item.split('\n'))
        datalist=item.split('\n')
        if datalist[1] in states:
            #print(datalist)
            n_Title="Covid-19 cases:"
            n_Text=f"{datalist[1]}:\nTotal Cases: {datalist[2]}:\nCured People: {datalist[3]}:\nDeaths: {datalist[4]}"
            notifyme(n_Title,n_Text)
            time.sleep(60*60)
