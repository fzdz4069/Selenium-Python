# Opening an HTML file with chromedriver and analyzing which links inside the file are working (all the files are attached in fz_html.zip).
# Creating a new table in MySQL and recording the test result for each link.

import mysql.connector
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("file:///D:/temp/fz_html/main/index.html")
driver.maximize_window()

new_tab = Keys.CONTROL + Keys.ENTER
albums = driver.find_elements(By.CLASS_NAME, "album")

link_titles = []
page_titles = []

for album in albums:
    album.send_keys(new_tab)
    link_titles.append(album.text)

whs = driver.window_handles
for window in whs:
    driver.switch_to.window(window)
    page_titles.append(driver.title)

driver.quit()
page_titles.remove(page_titles[0])
page_titles.reverse()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abcde12345",
    database="python")

cursor = mydb.cursor(buffered=True)
cursor.execute("CREATE table fz_html ("
               "number int primary key auto_increment,"
               "link_title varchar(100),"
               "page_title varchar(100),"
               "result varchar(30));")

n = 0
while n < len(link_titles):
    link_title = link_titles[n]
    page_title = page_titles[n]
    if link_title.lower() == page_title.lower():
        result = "Link works."
    elif page_title.startswith("file"):
        result = "Link doesn't work."
    else:
        result = "Link works, different title."

    insert = "insert into fz_html (link_title, page_title, result) values (%s, %s, %s)"
    value = (link_title, page_title, result)
    cursor.execute(insert, value)
    n += 1

cursor.execute("select * from fz_html")
for col in cursor:
    print(col)

mydb.commit()
cursor.close()
mydb.close()
