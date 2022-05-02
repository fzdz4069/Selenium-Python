# Testcase 9: Using a search engine, filtering videos by a specific xpath, and getting links.

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
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div[1]/div/ul[1]/li[3]/a").click()
sleep(3)
driver.get_screenshot_as_file("ddg09.png")
vids = driver.find_elements(By.XPATH, "//*[contains(text(), 'Python')]//ancestor::a")
print(len(vids))

for vid in vids:
    link = vid.get_attribute("href")
    print(link)

condition = len(vids) > 0
record_test("9", "duckduckgo.com", "Filtering videos in a search engine", condition)

driver.close()
