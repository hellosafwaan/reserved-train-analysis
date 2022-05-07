from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
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

def pages_and_rows() -> tuple:
    n = int(driver.find_element(By.XPATH, xpaths['page_details']).text.split(" ")[-1])
    if (n / 10 <= 1):
        total_pages = 1
        last_page_rows = n
    else:
        if n / 10 > n // 10:
            total_pages = (n // 10) + 1
            last_page_rows = n % 10
        else:
            total_pages = n // 10
            last_page_rows = 10
    return (total_pages, last_page_rows)

def collect_page(no_of_rows) -> list:
    page_data = []
    for j in range(2, no_of_rows + 2):
        row = []
        for k in range(1,6):
            td = driver.find_element(By.XPATH, xpaths['tableData'].format(j, k))
            row.append(td.text)
        page_data.append(row)
    return page_data

def collect_coach_data(coach_name) -> None:
    driver.find_element(By.XPATH, xpaths['coach_sort_button']).click()
    total_pages, last_page_rows = pages_and_rows()
    coach_data = []
    current_page = 1
    for i in range(total_pages):
        if (current_page == total_pages):
            coach_data += collect_page(last_page_rows)
        else:
            coach_data += collect_page(10)    
            nextPage = driver.find_element(By.XPATH, xpaths['next_page_button'])
            driver.execute_script('arguments[0].click()', nextPage)
        current_page += 1
    pd.DataFrame(coach_data, columns= get_headers()).to_csv("{}.csv".format(coach_name), index = False)
