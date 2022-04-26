# Testcase 6: Opening links in new tabs and taking sreenshots with specified names.

from record_test import record_test
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.donlope.net/fz/lyrics/")
driver.maximize_window()

albums = driver.find_elements(By.CLASS_NAME, "album")
print(len(albums))

n = 0
new_tab = Keys.CONTROL + Keys.ENTER
for album in albums:
    while n < 10:
        albums[n].send_keys(new_tab)
        n += 1

whs = driver.window_handles
for window in whs:
    driver.switch_to.window(window)
    title = driver.title
    driver.get_screenshot_as_file(title + ".png")

condition = len(albums) == 174
record_test("6", "donlope.net/fz/lyrics", "Opening links in new tabs", condition)

driver.quit()
