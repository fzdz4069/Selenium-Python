# Testcase 3: Testing "click" interactions on links and recording the test result in the database.

import mysql.connector
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abcde12345",
    database="python")

cursor = mydb.cursor()
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

insert = "insert into pytest(website, testcase) values (%s, %s)"
test3 = ("bitchute.com", "Test click interactions on links")
query_t = "update pytest set result='passed' where test_id=3"
query_f = "update pytest set result='failed' where test_id=3"
cursor.execute(insert, test3)

if url == expected_url:
    cursor.execute(query_t)
else:
    cursor.execute(query_f)

query = "select * from pytest"
cursor.execute(query)

for col in cursor:
    print(col)

mydb.commit()
cursor.close()
mydb.close()
driver.close()
