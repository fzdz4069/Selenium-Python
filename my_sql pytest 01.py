# Testcase 1: A basic test of chromedriver and of the function call to record test results.

from record_test import record_test
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://live.techpanda.org/index.php/")
driver.maximize_window()
title = driver.title
expected_title = "Home page"

condition = title == expected_title
record_test("1", "techpanda.org", "Testing function call", condition)

driver.close()
