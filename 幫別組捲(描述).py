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
    url="https://www.watsons.com.tw/%E5%87%B1%E5%A9%B7-%E9%9B%B6%E7%91%95%E8%82%8C%E5%AF%86%E8%9C%9C%E7%B2%89z-%E6%8E%A7%E6%B2%B9-6g/p/BP_251204"
    
    #response = requests.get(url,headers=headers)
    
    service = Service(executable_path="./msedgedriver.exe")
    driver = webdriver.Edge(service=service,options=Edge_options)
    
    driver.get(url)
    time.sleep(5)  # 等待 5 秒，讓頁面加載
    
    html = driver.page_source
    
    #解析
    #soup=BeautifulSoup(html,"html.parser")
    soup=BeautifulSoup(html,"html.parser")
    
    
    #urls = soup.select('h2.productName a')
    #打印HTML
    

    #names = soup.find_all('div', class_="product-name")
    names = soup.find_all('div', class_='product-name')
    print(names)
    """
    for name in names:
        print("品名:"+name.text)
    """
    #urls=soup.find_all('div', class_="item")
    #urls=urls.select('img')
    """
    moneys = soup.select('div.display-price span.price')
    print("價格:"+moneys[0].text)
    """
    """
    contents = soup.select('div.longDesc p')
    print("描述:")
    for content in contents:
        print(content.text)
    """
    """
    specTitles = soup.select('table.ecTable td.td1')
    specContents = soup.select('table.ecTable td.td2')
    specTitleBox=[]
    specContentBox=[]
    for specTitle in specTitles:
        
        #print(specTitle.text)
        tmp=specTitle.text
        specTitleBox.append(tmp)

    for specContent in specContents:
        #print(specContent.text)
        tmp=specContent.text
        specContentBox.append(tmp)
    
    for i in range(len(specTitleBox)):
        print(specTitleBox[i] + ":" + specContentBox[i])
"""
    #print("第"+str(i+1)+"頁---------------------------")
    
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

    