"""
This file is for testing the extraction from one page
This will be applied to the main file for going through all the page_source

@author: Mckelle Carr
"""

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
#delete after testing
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/mckellecarr/Downloads/chromedriver")
driver.get('https://www.noomii.com/life-coaches')
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html5lib')

users = []

for tag in soup.find('div', {'id': 'content'}).findAll('div', {'class':'coach row clear'}) :
    users.append(tag.get('id'))

users = list(filter(None.__ne__, users))

for coach in users:

    name = soup.find('div', {'id' : coach}).find('h4').find('a').get_text()

    job = soup.find('div', {'id' : coach}).find('p', {'class' : 'bold'}).get_text()

    location = soup.find('div', {'id' : coach}).find('address').get_text()

    phone = soup.find('div', {'id' : coach}).find('div', {'class' : 'contact col-sm-5 col-lg-4'}).find('p').get_text()
