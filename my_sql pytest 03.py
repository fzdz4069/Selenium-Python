# Testcase 3: Testing "click" interactions on links and recording the test result in the database.

from record_test import record_test
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.bitchute.com/")
driver.maximize_window()

# noinspection PyDeprecation
driver.find_element_by_xpath("//*[@id='alert-cookie']/div/p/button").click()
# noinspection PyDeprecation
driver.find_element_by_xpath("//*[@id='page-detail']/div/div[1]/div[1]/ul/li[3]/a").click()
# noinspection PyDeprecation
driver.find_element_by_xpath("//*[contains(text(), 'documentary')]").click()

url = driver.current_url
expected_url = "https://www.bitchute.com/hashtag/documentary/"
print(url)
assert url == expected_url
driver.get_screenshot_as_file("bitchute.png")

condition = url == expected_url
record_test("3", "bitchute.com", "Testing click interactions on links", condition)

driver.close()
