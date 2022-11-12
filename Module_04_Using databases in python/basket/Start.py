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
            create_database = "CREATE DATABASE `Basket`"
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
        database="Basket",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:

        with connection.cursor() as cursor:
            create_table1 = "CREATE table `clients` (id int auto_increment, name varchar(30), login varchar(30) UNIQUE, password varchar(30), PRIMARY KEY (id));"
            create_table2 = "CREATE table `product` (id int auto_increment, nameProduct varchar(30) UNIQUE, price int, PRIMARY KEY (id));"
            create_table3 = "CREATE table `Basket` (id int auto_increment, nameProduct varchar(30), price int, PRIMARY KEY (id));"
            cursor.execute(create_table1)
            cursor.execute(create_table2)
            cursor.execute(create_table3)
            create_table4 = f'insert into basket.product (nameProduct, price) values ("Samsung A-321", 5231), ("OPPO J-321", 5423), ("Samsung M-21", 9523), ("Nokia J-23", 6524);'
            cursor.execute(create_table4)
            connection.commit()
            print("Well done. Create table")

    finally:
        connection.close()

except:
    print("Error")
