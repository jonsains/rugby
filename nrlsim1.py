from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import numpy
import pandas as pd
from datetime import timedelta
from datetime import datetime
import csv

browser = webdriver.Chrome()
#create a csv file with all fixtures where % wins for each league fixture can be added
listoffixtures = []
browser.get("https://www.nrl.com/draw/")


check1 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//p[@class='match-team__name match-team__name--away']")))
print(check1.text)
check = browser.find_element_by_class_name('match-team__name match-team__name--away')
print(check.text)
hometeam = browser.find_elements_by_class_name('match-team__name match-team__name--home')
hometeams = []
print(len(hometeam))
for team in hometeam:
	print(team.text)
	hometeams.append(team.text)

awayteam = browser.find_elements_by_class_name('match-team__name match-team__name--away')
awayteams = []
for team in awayteam:
	print(team.text)
	awayteams.append(team.text)

winchance = [50 for team in awayteam]

df = pd.DataFrame({'home team': hometeams, 'away team': awayteams, 'home win %': winchance})
df.to_csv('round1fixturestest.csv', encoding='utf-8')
