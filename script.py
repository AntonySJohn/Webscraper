from selenium import webdriver
#import time
#import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
#chrome_driver = os.getcwd() +"\\chromedriver.exe"
#options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
print("Enter search query")
search = input()
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
#driver.minimize_window()
#driver.delete_all_cookies
#driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()
#driver.minimize_window() 
driver.get("https://www.geeksforgeeks.org/")
driver.delete_all_cookies()
driver.find_element_by_id('gsc-i-id2').click()
driver.find_element_by_id('gsc-i-id2').send_keys(search)
driver.find_element_by_id('gsc-i-id2').send_keys(Keys.ENTER)
#test = driver.find_element_by_class_name('gsc-webResult gsc-result')
#test = driver.find_elem
#url = driver.find_element_by_class_name('gsc-results-wrapper-overlay')
fastrack = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="___gcse_1"]/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[2]')))
URL = str(fastrack.text)
driver.get(URL)
driver.maximize_window()
driver.close()
newdriver = webdriver.Chrome()
newdriver.maximize_window()
newdriver.get(URL)
#driver.maximize_window()
#print(fastrack.text)
#url = driver.find_element_by_xpath('//*[@id="___gcse_1"]/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[2]')
#print(url.text)
#print(test)
#time.sleep(3)

