# Creating a table in MySQL and testing connection.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abcde12345",
    database="python")

cursor = mydb.cursor()

cursor.execute("CREATE table pytest ("
               "test_id int primary key auto_increment,"
               "website varchar(50),"
               "testcase varchar(50),"
               "result varchar(10));")

insert = "insert into pytest(test_id, website, testcase) values (%s, %s, %s)"
test1 = (0, 'database test', 'Testing connection')
query = "select * from pytest"
query_t = "update pytest set result='passed' where test_id=0"
query_f = "update pytest set result='failed' where test_id=0"
cursor.execute(insert, test1)
cursor.execute(query)

for col in cursor:
    if col[0] == 0:
        cursor.execute(query_t)
    else:
        cursor.execute(query_f)

cursor.execute(query)

for col in cursor:
    print(col)

mydb.commit()
cursor.close()
mydb.close()
