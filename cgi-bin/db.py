#!/usr/bin/env python3

import cgi

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def insert_data_into_database(host, db, username, password, query):
    status = 0
    try:
        connection = mysql.connector.connect(host=host,
                                             database=db,
                                             user=username,
                                             password=password)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        status = 0
        cursor.close()

    except mysql.connector.Error as error:
        status = 1


    finally:
        if (connection.is_connected()):
            connection.close()

    return status

form = cgi.FieldStorage()

my_query = f"INSERT INTO `info` (`user_id`,`user_password`,`first_name`,`last_name`,`gender`) VALUES (" \
           f"'{form.getvalue('userid')}'," \
           f"'{form.getvalue('password')}'," \
           f"'{form.getvalue('firstname')}'," \
           f"'{form.getvalue('lastname')}'," \
           f"'{str(form.getvalue('gender'))[0].capitalize()}');"

result = insert_data_into_database('127.0.0.1', 'db', 'username', 'password', my_query)

print("Content-Type: text/html")
print()    

print("<TITLE>Submission Successful</TITLE>" if not result else "<TITLE>Submission Failed</TITLE>")
print("<H2>User info added in database.</H2>" if not result else "<H2>Data entry failed; possible duplicate, check logs.</H2>")

