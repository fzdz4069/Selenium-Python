# Testcase 2: Testing page title and recording the test result in the database.

from record_test import record_test
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.donlope.net/fz/lyrics/")
driver.maximize_window()

title = driver.title
expected_title = "FZ Discography"
assert title.lower() == expected_title.lower()
print(title)

condition = title.lower() == expected_title.lower()
record_test("2", "donlope.net/fz/lyrics", "Testing page title", condition)

driver.close()
