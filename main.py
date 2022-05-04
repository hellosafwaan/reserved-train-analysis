from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)

def journeyDetails(trainNum, stationName, jDate) -> None:
    print(f'collecting data for {trainNum}')
    driver.find_element(By.XPATH, xpaths['trainNoInput']).send_keys(trainNum, Keys.RETURN)
    station = driver.find_element(By.XPATH, xpaths['boardingStationInput'])
    station.send_keys(stationName)
    station.send_keys(Keys.RETURN)
    station.send_keys(Keys.RETURN)
    select_date(jDate)
    driver.find_element(By.XPATH, xpaths['trainChartButton']).click()