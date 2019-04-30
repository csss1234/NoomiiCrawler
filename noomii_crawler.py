"""

@author: Mckelle Carr
"""
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import parametersNoomii
from time import sleep
from bs4 import BeautifulSoup
from parsel import Selector #for scraping
import csv
import re

#loop needs to go through all 274 pages until class = next_page_disabled
#within the loop it will collect the information and then navigate to the next page

def scrape_noomii(driver, website, csv_file):

    driver.get(website)

    with open(csv_file, 'w') as file:

        writer = csv.writer(file)
        writer.writerow(['Name','Job Title', 'Location', 'Phone Number'])

        next = driver.find_element_by_class_name('next_page')

        while next:


            sel = Selector(text=driver.page_source)
            html_source = driver.page_source
            soup = BeautifulSoup(html_source, 'html5lib')
            #make a list of ids that contain the word user.
            names = []
            for tag in soup.find('div', {'id': 'content'}).findAll('div', {'class':'coach row clear'}) :
                names.append(tag.get('id'))
            names = list(filter(None.__ne__, names))

            for coach in names:

                name = soup.find('div', {'id' : coach}).find('h4').find('a').get_text()

                job = soup.find('div', {'id' : coach}).find('p', {'class' : 'bold'}).get_text()

                location = soup.find('div', {'id' : coach}).find('address').get_text()

                phone = soup.find('div', {'id' : coach}).find('div', {'class' : 'contact col-sm-5 col-lg-4'}).find('p').get_text()

                writer.writerow([name, job, location, phone])

            try:
                next = soup.find('li', {'class' : 'next_page'}).find_all('a', href = True)
                for a in next:
                    link = 'https://www.noomii.com' + a['href']
                driver.get(link)
                # driver.find_element_by_xpath(link).click();
            except NoSuchElementException:
                next = None
    print("All Done!")

            #at the end of every loop, set next again so that we can continue the loop
            #until next cant find that class name
