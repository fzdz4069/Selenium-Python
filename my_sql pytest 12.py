# Testcase 12: Downloading multiple files.

import pytest
from record_test import record_test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

path = "d:\\temp\\down"
prefs = {"download.default_directory": path}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://chromedriver.chromium.org/downloads")
xpath = "//*[@id='h.e02b498c978340a_87']/div/div/ul[1]/li[1]/p/span[5]/a"
link = driver.find_element(By.XPATH, xpath).get_attribute("href")
driver.get(link)
sleep(3)

n = 4
while n <= 7:
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[" + str(n) + "]/td[2]/a").click()
    n += 1
    sleep(3)
driver.close()

files = os.listdir(path)
condition = len(files) == 4
record_test("12", "chromedriver.chromium.org", "Downloading multiple files", condition)
