from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from xpaths import xpaths

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)

def journey_details(train_num, station_name, j_date) -> None:
    print(f'collecting data for {train_num}')
    driver.find_element(By.XPATH, xpaths['train_no_input']).send_keys(train_num, Keys.RETURN)
    station = driver.find_element(By.XPATH, xpaths['boarding_station_input'])
    station.send_keys(station_name)
    station.send_keys(Keys.RETURN)
    station.send_keys(Keys.RETURN)
    select_date(j_date)
    driver.find_element(By.XPATH, xpaths['train_chart_button']).click()