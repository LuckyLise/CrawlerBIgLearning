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

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
    
Edge_options = Options()
#Edge_options.add_argument("--headless")
page=1
for i in range(page):
    url="https://www.watsons.com.tw/%E5%8C%96%E5%A6%9D%E5%93%81/%E7%9C%BC-%E7%9C%89%E5%BD%A9%E5%A6%9D/c/104402?currentPage="+str(i)
    
    #response = requests.get(url,headers=headers)
    
    service = Service(executable_path="./msedgedriver.exe")
    driver = webdriver.Edge(service=service,options=Edge_options)
    
    driver.get(url)
    
    html = driver.page_source
    
    #解析
    soup=BeautifulSoup(html,"html.parser")
    
    
    #urls = soup.select('h2.productName a')
    urls = soup.find_all('div', class_="formatted-value")
   
    #urls=soup.find_all('div', class_="item")
    #urls=urls.select('img')
    money=[]

    for url in urls:    
        if (len(url.text) != 0):
            print(url.text)
            money.append(url.text)


    print("第"+str(i+1)+"頁---------------------------")
    
driver.close()
        
    
    
    
    
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
#商品內文
#print(url["href"])
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

    