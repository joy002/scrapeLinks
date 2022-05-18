from cgitb import text
from os import link
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

fileName = "100Links.csv"
#read links from csv file
links = pd.read_csv(fileName)
print(links)

PATH = "/Users/yuting/chromedriver"
# driver instance in chrome
driver = webdriver.Chrome(PATH)

#driver.get(links['Links'][4])
#header = driver.title
#driver.find_element_by_id('main-content')
#print(header)

#all = driver.find_element_by_xpath("/html/body").text
#start = header in all
#all = all[start:]
#all = driver.find_elements(By.TAG_NAME("body"))
#print(all)

for i in range(len(links)):
    driver.get(links['Links'][i])
    header = driver.title
    all = driver.find_element_by_xpath("/html/body").text
    newF = str(i) + ".txt"
    #f = open('/Users/yuting/ScrapeLinks', 'w')
    with open(newF, 'w') as f:
       f.write(all)

    f.close()   
