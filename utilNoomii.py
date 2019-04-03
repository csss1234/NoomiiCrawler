"""

@author: Mckelle Carr
"""
from selenium import webdriver
import parametersNoomii
import noomii_crawler

parametersNoomii.website_URL='https://www.noomii.com/life-coaches'

website = parametersNoomii.website_URL
driver = webdriver.Chrome(executable_path="/Users/mckellecarr/Downloads/chromedriver")

noomii_crawler.scrape_noomii(driver, website, parametersNoomii.results_Noomii)
