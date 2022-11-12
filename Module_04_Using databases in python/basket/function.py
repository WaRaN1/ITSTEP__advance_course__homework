import pymysql
from easygui import *
# from main import *


def registration(connection):
    while True:
        log = enterbox("Введіть логін", "Реєстрація")
        with connection.cursor() as cursor:
            select = "SELECT * FROM basket.clients;"
            cursor.execute(select)
            result = cursor.fetchall()
            print(result)
            if len(result) == 0:
                passw = multpasswordbox("Введіть ім'я(буквами) та пароль(цифрами)", "Password", ["Iм'я", "Password"])
                with connection.cursor() as cursor:
                    insert = f"insert into basket.clients (name, login, password) values ('{passw[0]}', '{log}', {int(passw[1])});"
                    print(insert)
                    cursor.execute(insert)
                    connection.commit()
                return "Yes"
            else:
                for i in result:
                    if log == i["login"]:
                        msgbox("Такий логін вже використовується", "Реєстрація")
                        break
                    else:
                        passw = multpasswordbox("Введіть ім'я та пароль(цифрами)", "Password", ["Iм'я", "Password"])
                        with connection.cursor() as cursor:
                            insert = f"insert into basket.clients (name, login, password) values ('{passw[0]}', '{log}', {int(passw[1])});"
                            print(insert)
                            cursor.execute(insert)
                            connection.commit()
                        return "Yes"


def authorization(connection):
    var = "No"
    while True:
        log_pass = multpasswordbox("Введіть логін та пароль(цифрами)", "Password", ["login", "password"])
        with connection.cursor() as cursor:
            select = "SELECT * FROM basket.clients;"
            cursor.execute(select)
            result = cursor.fetchall()
        for i in result:
            if log_pass[0] != i["login"]:
                msgbox("Невірно введений логін", "Реєстрація")
                break
            elif log_pass[0] == i["login"] and log_pass[1] != i["password"]:
                msgbox("Невірно введений пароль", "Реєстрація")
                break
            elif log_pass[0] == i["login"] and log_pass[1] == i["password"]:
                a = msgbox("Вхід дозволено")
                var = "Yes"
                break
        return var




try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="12921292a",
        database="Basket",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:
        def shop(connection):
            with connection.cursor() as cursor:
                create_database = "SELECT * FROM basket.product;"
                cursor.execute(create_database)
                result = cursor.fetchall()
            txt_v = "Shop:\n"
            for var in result:
                txt_v = txt_v + f"{var['nameProduct']}, price: {var['price']}\n"
            return txt_v

        def choice_shop(connection):
            with connection.cursor() as cursor:
                create_database = "SELECT * FROM basket.product;"
                cursor.execute(create_database)
                result = cursor.fetchall()
            lst_v = []
            for var in result:
                lst_v.append(var['nameProduct'])
            return lst_v


        def basket(connection):
            with connection.cursor() as cursor:
                create_database = "SELECT * FROM basket.basket;"
                cursor.execute(create_database)
                result = cursor.fetchall()
            txt_v = "Basket:\n"
            for var in result:
                txt_v = txt_v + f"{var['nameProduct']}, price: {var['price']}\n"
            return txt_v


        def add_basket(connection):
            choice = buttonbox(shop(connection), "Basket", choice_shop(connection))
            with connection.cursor() as cursor:
                create_database = f"SELECT * FROM basket.product where nameProduct = '{choice}';"
                cursor.execute(create_database)
                result = cursor.fetchall()
                a = msgbox(f"Product {choice} added")
            with connection.cursor() as cursor:
                create_database = f"insert into basket.basket (nameProduct, price) values ('{result[0]['nameProduct']}', '{result[0]['price']}');"
                cursor.execute(create_database)
                connection.commit()
            return "Yes"


        def choice_basket(connection):
            with connection.cursor() as cursor:
                create_database = "SELECT * FROM basket.basket;"
                cursor.execute(create_database)
                result = cursor.fetchall()
            lst_v_b = []
            for var in result:
                lst_v_b.append(var['nameProduct'])
            return lst_v_b


        def delete_basket(connection):
            choice = buttonbox(basket(connection), "Basket", choice_basket(connection))
            with connection.cursor() as cursor:
                create_database = f"SELECT * FROM basket.basket where nameProduct = '{choice}';"
                cursor.execute(create_database)
                result = cursor.fetchall()
            with connection.cursor() as cursor:
                create_database = f"DELETE FROM basket.basket WHERE id = {result[0]['id']};"
                cursor.execute(create_database)
                connection.commit()
                a = msgbox(f"Product {choice} delete")
            return "Yes"


        def update_basket(connection):
            choice = buttonbox(basket(connection), "Basket", choice_basket(connection))
            with connection.cursor() as cursor:
                create_database = f"SELECT * FROM basket.basket where nameProduct = '{choice}';"
                cursor.execute(create_database)
                result = cursor.fetchall()
            choice2 = buttonbox(f"{result[0]['nameProduct']}, price: {result[0]['price']}\n \nЩо бажаєте змінити?", "Basket", ['nameProduct', 'price'])
            choice3 = enterbox(f"Введіть новий {choice2}", )
            with connection.cursor() as cursor:
                if choice2 == 'price':
                    create_database = f"UPDATE basket.basket SET {choice2} = {choice3} WHERE id = '{result[0]['id']}';"
                elif choice2 == 'nameProduct':
                    create_database = f"UPDATE basket.basket SET {choice2} = '{choice3}' WHERE id = '{result[0]['id']}';"
                cursor.execute(create_database)
                connection.commit()
                a = msgbox(f"Product {choice} update")
            return "Yes"


        def truncate_basket(connection):
            with connection.cursor() as cursor:
                create_database = f"TRUNCATE basket.basket;"
                cursor.execute(create_database)
                connection.commit()
                a = msgbox(f"Basket cleared")
            return "Yes"


        def search_basket(connection):
            choice = enterbox("Який товар шукаєте?")
            if choice in choice_basket(connection):
                with connection.cursor() as cursor:
                    create_database = f"SELECT * FROM basket.basket WHERE nameProduct = '{choice}';"
                    cursor.execute(create_database)
                    result = cursor.fetchall()
                    a = msgbox(f"{choice}, price: {result[0]['price']}")
            else:
                msgbox("No")
            return "Yes"




    finally:
        connection.close()

except:
    print("Error")


