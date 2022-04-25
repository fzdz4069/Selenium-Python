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

driver.get("https://www.donlope.net/fz/lyrics/")
driver.maximize_window()
title = driver.title
expected_title = "FZ Discography"
assert title.lower() == expected_title.lower()
print(title)

insert = "insert into pytest(website, testcase) values (%s, %s)"
test2 = ("donlope.net/fz/lyrics", "Test page title")
query_t = "update pytest set result='passed' where test_id=2"
query_f = "update pytest set result='failed' where test_id=2"
cursor.execute(insert, test2)

if title.lower() == expected_title.lower():
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
