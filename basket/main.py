import pymysql
from easygui import *
from function import *

passw = enterbox("Enter your password for Database", "Password")

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
        choice = 0
        while choice != "Відміна":
            choice = buttonbox("Привіт, щоб почати покупки необхідно авторизуватись", "Authorizationr", ["Авторизація", "Реєстрація", "Відміна"])
            if choice == "Реєстрація":
                registration(connection)
            elif choice == "Авторизація":
                if authorization(connection) == "Yes":
                    while choice != "Відміна":
                        choice = buttonbox(shop(connection), "Shop", ["Додати товар у кошик", "Видалити товар з кошика",
                                                                   "Змінити товар у кошику", "Повне очищення кошика",
                                                                   "Пошук даних у кошику", "Перегляд вмісту кошика",
                                                                   "Відміна"])
                        if choice == "Додати товар у кошик":
                            add_basket(connection)
                        if choice == "Видалити товар з кошика":
                            delete_basket(connection)
                        if choice == "Змінити товар у кошику":
                            update_basket(connection)
                        if choice == "Повне очищення кошика":
                            truncate_basket(connection)
                        if choice == "Пошук даних у кошику":
                            search_basket(connection)
                        if choice == "Перегляд вмісту кошика":
                            a = msgbox(basket(connection))


    finally:
        connection.close()

except:
    print("Error")
