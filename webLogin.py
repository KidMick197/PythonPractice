# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:22:58 2019

@author: Mickey Glover
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

userName=input('Enter Your LinkedIn Email: ')
passWord=input('Enter Your LinkedIn Password: ')
print(userName +' '+ passWord)
url= 'https://www.linkedin.com'
search=''
search=input("What do you want to search: ")
hrefList=[]
skillsList=[]
i=300

driver=webdriver.Chrome('C:/Users/Mickey/Downloads/chromedriver_win32/chromedriver')
action= ActionChains(driver)
driver.get(url)
driver.find_element_by_class_name('nav__button-secondary').click()
driver.find_element_by_id('username').send_keys(userName)
driver.find_element_by_id('password').send_keys(passWord)
driver.find_element_by_class_name('btn__primary--large').click()


driver.find_element_by_class_name('search-global-typeahead__input').send_keys(search)
driver.find_element_by_class_name('search-global-typeahead__input').send_keys(Keys.ENTER) 
#driver.find_element_by_css_selector('a[href*="/search/results/people/"]').click()
time.sleep(5)
driver.find_element_by_xpath("//*[@aria-label='View only People results']").click()
time.sleep(5)
content_blocks=driver.find_elements_by_css_selector("div[class='search-result__info pt3 pb4 ph0'] a[class='search-result__result-link ember-view']")
for block in content_blocks:
    hrefList.append(block.get_attribute('href'))
for i,href in enumerate(hrefList):
        driver.get(hrefList[i])
        time.sleep(3)

#      --------------------  THIS IS WHERE I AM HAVING AN ERROR!---------------------
        driver.find_element_by_xpath("//button[class= 'pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid']").click()
        time.sleep(3)


print(hrefList)    
driver.get(url)
