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
