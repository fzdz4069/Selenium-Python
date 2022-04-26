# Testcase 4: Logging in with email and password.
# Testcase 5: Logging out.

from record_test import record_test
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("http://live.techpanda.org/index.php/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='header']/div/div[2]/div/a").click()
driver.find_element(By.XPATH, "//*[@id='header-account']/div/ul/li[1]/a").click()
driver.find_element(By.ID, "email").send_keys("qabcdeq@xyz.com")
driver.find_element(By.ID, "pass").send_keys("qwerty")
driver.find_element(By.XPATH, "//*[@id='send2']/span/span").click()
sleep(3)

url = driver.current_url
expected_url = "http://live.techpanda.org/index.php/customer/account/index/"
assert url == expected_url
condition = url == expected_url
record_test("4", "techpanda.org", "Logging in", condition)

driver.find_element(By.XPATH, "//*[@id='header']/div/div[2]/div/a/span[2]").click()
driver.find_element(By.XPATH, "//*[@id='header-account']/div/ul/li[5]/a").click()
sleep(3)

url = driver.current_url
assert url != expected_url
condition = url != expected_url
record_test("5", "techpanda.org", "Logging out", condition)

driver.close()
