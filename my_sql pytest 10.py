# Testcase 10: Downloading a YouTube video in Chrome.

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

driver.get("https://www.duckduckgo.com/")
driver.find_element(By.XPATH, "//*[@id='search_form_input_homepage']").send_keys("software testing")
driver.find_element(By.XPATH, "//*[@id='search_button_homepage']").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div[1]/div/ul[1]/li[3]/a").click()
sleep(3)
video = driver.find_element(By.XPATH, "//*[@id='zci-videos']/div/div[2]/div/div[3]/div[2]/h6/a")
link = video.get_attribute("href")

driver.get('https://y2mate.is')
driver.find_element(By.XPATH, '//*[@id="txtUrl"]').send_keys(link)
driver.find_element(By.XPATH, "//*[@id='btnSubmit']/span[2]").click()
sleep(10)

xpath1 = "/html/body/section[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/button"
driver.find_element(By.XPATH, xpath1).click()
sleep(5)
xpath2 = "/html/body/section[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/button/a"
driver.find_element(By.XPATH, xpath2).click()
sleep(20)
driver.quit()

files = os.listdir(path)
condition = files[0].endswith(".mp4")
record_test("10", "y2mate.is", "Downloading a video in Chrome", condition)
