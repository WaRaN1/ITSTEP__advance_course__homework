import pymysql
from easygui import *

passw = enterbox("Enter your password for Database", "Password")

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password=passw,
        database="people",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:
        with connection.cursor() as cursor:
            create_database = "CREATE DATABASE `NewsFeed`"
            cursor.execute(create_database)
            print("Well done. Create database")
    finally:
        connection.close()

except:
    print("Error")

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password=passw,
        database="NewsFeed",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:

        with connection.cursor() as cursor:
            create_table1 = "CREATE table NewsFeed.`administrator` (id int auto_increment, name varchar(30), login varchar(30) UNIQUE, password varchar(30), PRIMARY KEY (id));"
            create_table2 = "CREATE table NewsFeed.`news` (id int auto_increment, title varchar(200) UNIQUE, autor varchar(30), date date, PRIMARY KEY (id));"
            cursor.execute(create_table1)
            cursor.execute(create_table2)
            connection.commit()
            print("Well done. Create table")

    finally:
        connection.close()

except:
    print("Error")
