from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import csv
import pandas as pd
from pandas import DataFrame
from selenium.common.exceptions import NoSuchElementException   




url = str(input("Nhap link san pham: "))
n=int(input("Nhap so trang can lay: "))
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get(url)

sleep(2)

authors=[]
times=[]
comments=[]
likes=[]


for j in range(n):
    divs=driver.find_elements_by_class_name("shopee-product-rating__main")
    for i in divs:
        sleep(2)
        author=[]
        comment=[]
        time=[]     
        like=[]
        
        try:
            author = i.find_element_by_class_name('shopee-product-rating__author-name')
            authors.append(author.text)
        except NoSuchElementException:
            authors.append("?")
            
        try:
            comment = i.find_element_by_class_name("_3NrdYc")
            comments.append(comment.text)
        except NoSuchElementException:
            comments.append("?")
        
        try:
            time = i.find_element_by_class_name("shopee-product-rating__time")
            times.append(time.text)
        except NoSuchElementException:
            times.append("?")
        
        try:
            like=i.find_element_by_class_name("shopee-product-rating__like-count")
            likes.append(like.text)
        except:
            likes.append("?")
        
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[2]/button[8]').click()
    sleep(4)

driver.close()

print(authors)
print(times)
print(comments)
print("----------------------")

data={"Author":authors,"Time and Type":times,"Comment":comments,"Like":likes}
df=DataFrame(data,columns=["Author","Time and Type","Comment","Like"])

df.to_csv("shopee_crawl.csv")