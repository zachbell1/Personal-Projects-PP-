#!/usr/bin/env python3

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from bs4 import Comment
from lxml import html
from urllib.request import urlopen

import pandas as pd
import numpy as np
import requests

import time
chrome_options = webdriver.ChromeOptions()



driver = webdriver.Chrome()
chrome_options.add_experimental_option('useAutomationExtension', "false")


driver.get('https://mint.intuit.com/')

creds1 = open ('/Users/zacharybell/Desktop/Python/creds.txt', 'r')
line = list('/Users/zacharybell/Desktop/Python/creds.txt')
for line in creds1:
	
	temp = line.strip().split(":") or both
	email = temp[0]
	passw = temp[1]

#NAVIGATE FROM SIGN IN TO TRANSACTIONS
signIn = driver.find_element(By.XPATH, '/html/body/div[1]/div/header/div[3]/div[1]/div/div[3]/a[2]')
signIn.click()

userbutton = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/section/div/div/div[2]/section[3]/div/section[1]/div/form/fieldset/div/input')))


UserId = driver.find_element(By.XPATH, '/html/body/section/section/div/div/div[2]/section[3]/div/section[1]/div/form/fieldset/div/input').send_keys(email) #change to creds.txt file

UserSignIn =driver.find_element(By.XPATH, '/html/body/section/section/div/div/div[2]/section[3]/div/section[1]/div/form/div[3]/button').click()



passbutton = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/section/div/div/div[2]/section[7]/div/section[4]/div/div[1]/form/fieldset[4]/div/input')))

enterPass = driver.find_element(By.XPATH, '/html/body/section/section/div/div/div[2]/section[7]/div/section[4]/div/div[1]/form/fieldset[4]/div/input').send_keys(passw) #change to creds.txt file


Continue = driver.find_element(By.XPATH, '/html/body/section/section/div/div/div[2]/section[7]/div/section[4]/div/div[1]/form/div[3]/input').click()

transaction_table = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/nav/div/div/div/div/div/ul/li[2]/a')))

Transactions = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/nav/div/div/div/div/div/ul/li[2]/a').click()

time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)

Display_100 = driver.find_element(By.XPATH, '/html/body/div[3]/div[6]/div/div[1]/div[7]/div[2]/div[9]/div[2]/div/table/tbody/tr/td[2]/div[3]/div[13]/p/a[3]')
Display_100.click()







#CREATE TRANSACTION LIST TO DATAFRAME THEN TO CSV
time.sleep(5)
df_transactions = pd.read_html(driver.find_element(By.ID, 'transaction-list').get_attribute('outerHTML'))[0]


#df_transactions.to_csv('transactions.csv')

df= pd.read_csv('/Users/zacharybell/Desktop/Python/transactions.csv', index_col=0, skiprows=2)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #deletes unamed columns
df.columns = ["Date","Transaction","Category","Amount"]
df.head()

df.to_csv('transactions.csv')
print(df)