import pymysql
from easygui import *
from function1 import *

passw = enterbox("Enter your password for Database", "Password")

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
        choice = 0
        while choice != "Відміна":
            choice = buttonbox("Привіт, щоб почати покупки необхідно авторизуватись", "Authorizationr", ["Авторизація", "Реєстрація", "Відміна"])
            if choice == "Реєстрація":
                registration(connection)
            elif choice == "Авторизація":
                if authorization(connection) == "Yes":
                    while choice != "Відміна":
                        choice = buttonbox(news(connection), "Newsfeed", ["Додати новину", "Видалити новину",
                                                                   "Змінити новину", "Повне очищення таблиці новин",
                                                                   "Переглянути стрічку новин", "Переглянути найсвіжішу новину",
                                                                   "Відміна"])
                        if choice == "Додати новину":
                            add_news(connection)
                        if choice == "Видалити новину":
                            delete_news(connection)
                        if choice == "Змінити новину":
                            update_news(connection)
                        if choice == "Повне очищення таблиці новин":
                            truncate_news(connection)
                        if choice == "Переглянути стрічку новин":
                            search_news(connection)
                        if choice == "Переглянути найсвіжішу новину":
                            max_date(connection)


    finally:
        connection.close()

except:
    print("Error")
