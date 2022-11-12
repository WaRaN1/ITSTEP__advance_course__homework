import pymysql
from easygui import *

userInter = enterbox("What's your name(root) in SQL?", "Password")
passw = enterbox("Enter your password for SQL", "Password")

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user=userInter,
        password=passw,
        database="sakila",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:
        with connection.cursor() as cursor:
            create_database = "CREATE DATABASE `socialnetwork`"
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
        user=userInter,
        password=passw,
        database="socialnetwork",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:

        with connection.cursor() as cursor:
            create_table1 = "CREATE TABLE `users` (id int auto_increment,Name nvarchar(100), Surname nvarchar(100),Login nvarchar(100) UNIQUE,Parol nvarchar(100),primary key (id));"
            create_table2 = "CREATE TABLE `friends` (id int auto_increment,Name nvarchar(100), Surname nvarchar(100),Login nvarchar(100),FriendLogin nvarchar(100),primary key (id), foreign key (Login) references `users` (Login));"
            create_table3 = "CREATE TABLE `posts` (id int auto_increment,postName nvarchar(100),Post nvarchar(1000), Login nvarchar(100),primary key (id),foreign key (Login) references `users` (Login));"
            first_users = "INSERT INTO `users` (Name,Surname,Login,Parol) VALUES ('Pavlo','Bezd','ADMIN','1234')"
            cursor.execute(create_table1)
            cursor.execute(create_table2)
            cursor.execute(create_table3)
            cursor.execute(first_users)
            connection.commit()
            print("Well done. Create table")

    finally:
        connection.close()

except:
    print("Error")