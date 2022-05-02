# Testcase 8: Using a search engine, filtering images from last month, and getting links.

from record_test import record_test
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.duckduckgo.com")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='search_form_input_homepage']").send_keys("selenium webdriver")
driver.find_element(By.XPATH, "//*[@id='search_button_homepage']").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div[1]/div/ul[1]/li[2]/a").click()
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/ol/li[5]/a").click()
sleep(3)
driver.get_screenshot_as_file("ddg08.png")
pics = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div//ancestor::a")
print(len(pics))

for pic in pics:
    link = pic.get_attribute("href")
    print(link)

condition = len(pics) > 0
record_test("8", "duckduckgo.com", "Filtering images in a search engine", condition)

driver.close()
