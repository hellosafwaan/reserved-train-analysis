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

def select_date(journey_date) -> None:
    journey_day = journey_date[8:10]
    if journey_day[0] == '0':
        journey_day = journey_day[1]
    driver.find_element(By.XPATH, xpaths['journey_date_input']).click()
    dates = driver.find_elements(By.XPATH, xpaths['date_buttons'])
    for d_elem in dates:
        if d_elem.text == journey_day and d_elem.get_attribute('tabindex') == '0':
            d_elem.click()
            break

def get_headers() -> list:
    headers = []
    for i in range(1, 6):
        th = driver.find_element(By.XPATH, xpaths['headers_data'].format(i))
        headers.append(th.text)
    return headers