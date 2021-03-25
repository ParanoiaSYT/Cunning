import requests
from bs4 import BeautifulSoup
import openpyxl
from fake_useragent import UserAgent
import re




def get_dara():
    url='http://poe.game.qq.com/character-window/get-characters'
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers, timeout=10)

    soup=BeautifulSoup(response.text,'lxml')
    lists=soup.find_all("li",class_='character')
    for i in lists:
        name=i.find('div',class_='infoLine2').text


        print(name)



get_dara()