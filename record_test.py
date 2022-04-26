# A function created to be called for recording test results in the MySQL database.

import mysql.connector


def record_test(test_id, website, testcase, condition):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="abcde12345",
        database="python")
    cursor = mydb.cursor()
    insert = "insert into pytest(test_id, website, testcase) values (%s, %s, %s)"
    test_n = (test_id, website, testcase)
    query_t = "update pytest set result='passed' where test_id=" + test_id
    query_f = "update pytest set result='failed' where test_id=" + test_id
    cursor.execute(insert, test_n)

    if condition:
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
