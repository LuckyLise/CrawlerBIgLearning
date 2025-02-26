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

#商品列表
url="https://www.watsons.com.tw/%E5%8C%96%E5%A6%9D%E5%93%81/%E7%B2%89%E9%A4%85-%E8%9C%9C%E7%B2%89/c/10440104"

Edge_options = Options()
service = Service(executable_path="./msedgedriver.exe")
driver = webdriver.Edge(service=service,options=Edge_options)

driver.get(url)

html = driver.page_source

#解析
soup=BeautifulSoup(html,"html.parser")

#個別商品網址
producturls = soup.select('a.ClickSearchResultEvent_Class')
producturlBox=[]
for producturl in producturls:
    if ("https://www.watsons.com.tw/"+str(producturl["href"]) not in producturlBox):
        producturlBox.append("https://www.watsons.com.tw/"+str(producturl["href"]))


for i in range(len(producturlBox)):
    url=producturlBox[i]
    
    driver.get(url)
    #https://www.watsons.com.tw/%E5%87%B1%E5%A9%B7-%E9%9B%B6%E7%91%95%E8%82%8C%E5%AF%86%E8%9C%9C%E7%B2%89z-%E6%8E%A7%E6%B2%B9-6g/p/BP_251204
    #這個網頁加載太慢所以要等
    time.sleep(5)  # 等待 5 秒，讓頁面加載 by GPT
    html = driver.page_source
    
    #解析
    soup=BeautifulSoup(html,"html.parser")
    
    moneys = soup.select('div.display-price span.price')
    names = soup.find_all('div', class_="product-name")
    print("品名:"+names[0].text)
    print("價格:"+moneys[0].text)
    print("第"+str(i+1)+"筆資料完成---------------------------")
    
driver.close()
        
    
 
    