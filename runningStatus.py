from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import  StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import pandas as pd
from datetime import date

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)

driver.get('https://enquiry.indianrail.gov.in/mntes/')
parent_window = driver.current_window_handle
driver.implicitly_wait(5)

def train_details(train_num):
    train_num_elem = driver.find_element(By.ID, 'trainNo')
    train_num_elem.send_keys(train_num)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="jStation"]/option[2]')))
    Select(driver.find_element(By.ID, 'jStation')).select_by_index('1')
    prev_day = driver.find_element(By.ID, "jYesterday")
    try:
        prev_day.click()
    except StaleElementReferenceException as e:
        prev_day = driver.find_element(By.ID, "jYesterday").click()
