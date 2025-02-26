# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:43:44 2025

@author: user
"""
import os
import time
import requests

from bs4 import BeautifulSoup
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium import webdriver

def fetch_data(url):
    response= requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    titles=soup.find_all()
    print(titles)
    
Edge_options = Options()
Edge_options.add_argument("--headless")


service = Service(executable_path="./msedgedriver.exe")
driver = webdriver.Edge(service=service,options=Edge_options)

driver.get('https://www.allride.com.tw/product/detail/19997')

html = driver.page_source

#解析
soup=BeautifulSoup(html,"html.parser")

"""
titles=soup.find_all('h4', class_="card-text")
dates=soup.find_all('p', class_="card-text")
urls=soup.find_all('div', class_="card-body")
titles_result=[]
dates_result=[]
urls_result=[]
#標題
for title in titles:
    try:
        titles_result.append(title.text)
    except:
        pass

#日期
for date in dates:
    try:
        dates_result.append(date.text)
    except:
        pass
#內文超連結
for url in urls:
    try:
        urls_result.append(url.find('a').get('href'))
    except:
        pass

for url in urls:
    try:
        urls_result.append(url)
    except:
        pass


print(titles_result)
print(urls_result)


"""
urls = soup.select('div.item img')
#urls=soup.find_all('div', class_="item")
#urls=urls.select('img')

for url in urls:    
    print("https://www.allride.com.tw/"+url["src"].split("&")[0])

"""

imgs=soup.find_all('img')
for img in imgs:
    try:
        url = img['src']
        
        filename = img['alt']

        resp=requests.ger(url)
        
        img = resp.content
        os.makedirs('images',exist_ok=True)
        #wb 二元寫入，寫入圖片用
        with open(f'images/{filename}.png','wb') as f:
            f.write(img)
    
        #print(f'{name} - {url}')
        
    except:
        pass
"""
driver.close()
    
    