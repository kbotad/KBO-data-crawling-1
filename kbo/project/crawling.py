from selenium import webdriver
import pandas as pd
import os
import numpy as np # linear algebra
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import time


chrome_path = "/Users/seungsoo/Documents/GitHub/kbo/project/chromedriver"  
driver = webdriver.Chrome(executable_path = chrome_path)  



def crawling(year):
    url1= "https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx" 
    driver.get(url1) 
    response = requests.get(url1)
    driver.find_element_by_xpath(f'//select[@name="ctl00$ctl00$ctl00$cphContents$cphContents$cphContents$ddlSeason$ddlSeason"]/option[text()={year}]').click()
    time.sleep(1)
    html = driver.page_source
#    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.select('table')
    table = tables[0]
    table_html = str(table)
    table_df_list = pd.read_html(table_html)
    table_df = table_df_list[0]
    table_df.to_csv(f'/Users/seungsoo/Documents/GitHub/kbo/project/data/{year}.csv', index=False)
    
    url2= "https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic2.aspx" 
    driver.get(url2) 
    response = requests.get(url2)
    driver.find_element_by_xpath(f'//select[@name="ctl00$ctl00$ctl00$cphContents$cphContents$cphContents$ddlSeason$ddlSeason"]/option[text()={year}]').click()
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.select('table')
    table = tables[0]
    table_html = str(table)
    table_df_list = pd.read_html(table_html)
    table_df = table_df_list[0]
    table_df = table_df.iloc[:,4:]
    table_df.to_csv(f'/Users/seungsoo/Documents/GitHub/kbo/project/data/{year}_2.csv',index=False)


for year in range(2002, 2022):
    crawling(year);



#driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_ddlSeason_ddlSeason").click() 
#driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child(39)").click() 







