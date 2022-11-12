import pymysql
from easygui import *
# from main import *


def registration(connection):
    while True:
        log = enterbox("Введіть логін", "Реєстрація")
        with connection.cursor() as cursor:
            select = "SELECT * FROM NewsFeed.administrator;"
            cursor.execute(select)
            result = cursor.fetchall()
            print(result)
            if len(result) == 0:
                passw = multpasswordbox("Введіть ім'я(буквами) та пароль(цифрами)", "Password", ["Iм'я", "Password"])
                with connection.cursor() as cursor:
                    insert = f"insert into NewsFeed.administrator (name, login, password) values ('{passw[0]}', '{log}', {int(passw[1])});"
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
                            insert = f"insert into NewsFeed.administrator (name, login, password) values ('{passw[0]}', '{log}', {int(passw[1])});"
                            print(insert)
                            cursor.execute(insert)
                            connection.commit()
                        return "Yes"


def authorization(connection):
    var = "No"
    while True:
        log_pass = multpasswordbox("Введіть логін та пароль(цифрами)", "Password", ["login", "password"])
        with connection.cursor() as cursor:
            select = "SELECT * FROM NewsFeed.administrator;"
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
        database="NewsFeed",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:
        def news(connection):
            with connection.cursor() as cursor:
                create_database = "SELECT * FROM NewsFeed.news;"
                cursor.execute(create_database)
                result = cursor.fetchall()
            if len(result) == 0:
                txt_v = ""
            else:
                txt_v = "NewsFeed:\n"
                for var in result:
                    txt_v = txt_v + f"{var['autor']}, date: {var['date']}\n"
                return txt_v


        def add_news(connection):
            news = multenterbox("Your news", "News", ["title", "autor", "date"])
            with connection.cursor() as cursor:
                create_database = f"insert into NewsFeed.news (title, autor, date) values ('{news[0]}', '{news[1]}', '{news[2]}')"
                print(create_database)
                cursor.execute(create_database)
                connection.commit()
            return "Yes"


        def delete_news(connection):
            choice = multenterbox("Which news should be deleted, indicate the author and the publication number",
                                  "News", ["autor", "date"])
            with connection.cursor() as cursor:
                create_database = f"SELECT * FROM newsfeed.news where autor = '{choice[0]}' and date = '{choice[1]}';"
                cursor.execute(create_database)
                result = cursor.fetchall()
            with connection.cursor() as cursor:
                create_database = f"DELETE FROM newsfeed.news WHERE id = {result[0]['id']};"
                cursor.execute(create_database)
                connection.commit()
                a = msgbox(f"Product {choice[0]} by {choice[0]} delete")
            return "Yes"


        def update_news(connection):
            choice = multenterbox("Яку новину потрібно змінити, вкажіть автора та номер публікації",
                                  "News", ["autor", "date"])
            with connection.cursor() as cursor:
                create_database = f"SELECT * FROM newsfeed.news where autor = '{choice[0]}' and date = '{choice[1]}';"
                cursor.execute(create_database)
                result = cursor.fetchall()
            choice2 = buttonbox(f"{result[0]['autor']}, date: {result[0]['date']}\n \nЩо бажаєте змінити?",
                                "Basket", ['title', 'autor', 'date'])
            choice3 = enterbox(f"Введіть нове значення: {choice2}", )
            with connection.cursor() as cursor:
                if choice2 == 'title':
                    create_database = f"UPDATE newsfeed.news SET {choice2} = {choice3} WHERE id = '{result[0]['id']}';"
                elif choice2 == 'autor':
                    create_database = f"UPDATE newsfeed.news SET {choice2} = '{choice3}' WHERE id = '{result[0]['id']}';"
                elif choice2 == 'date':
                    create_database = f"UPDATE newsfeed.news SET {choice2} = '{choice3}' WHERE id = '{result[0]['id']}';"
                cursor.execute(create_database)
                connection.commit()
                a = msgbox(f"Update")
            return "Yes"


        def truncate_news(connection):
            with connection.cursor() as cursor:
                create_database = f"TRUNCATE newsfeed.news;"
                cursor.execute(create_database)
                connection.commit()
                a = msgbox(f"News cleared")
            return "Yes"


        def search_news(connection):
            with connection.cursor() as cursor:
                create_database = "SELECT * FROM NewsFeed.news;"
                cursor.execute(create_database)
                result = cursor.fetchall()
            if len(result) == 0:
                txt_v = "Лента порожня"
            else:
                txt_v = "NewsFeed:\n"
                for var in result:
                    txt_v = txt_v + f"{var['title']}\n {var['autor']}\n {var['date']}\n \n"
                a = msgbox(txt_v)
                return txt_v


        def max_date(connection):
            with connection.cursor() as cursor:
                create_database = f"select * from newsfeed.news where date = (select max(date) from NewsFeed.news);"
                cursor.execute(create_database)
                result = cursor.fetchall()
            if len(result) == 0:
                txt_v = "Лента порожня"
            else:
                txt_v = "NewsFeed:\n"
                for var in result:
                    txt_v = txt_v + f"{var['title']}\n {var['autor']}\n {var['date']}\n \n"
                a = msgbox(txt_v)
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


        # def add_basket(connection):
        #     choice = buttonbox(shop(connection), "Basket", choice_shop(connection))
        #     with connection.cursor() as cursor:
        #         create_database = f"SELECT * FROM basket.product where nameProduct = '{choice}';"
        #         cursor.execute(create_database)
        #         result = cursor.fetchall()
        #         a = msgbox(f"Product {choice} added")
        #     with connection.cursor() as cursor:
        #         create_database = f"insert into basket.basket (nameProduct, price) values ('{result[0]['nameProduct']}', '{result[0]['price']}');"
        #         cursor.execute(create_database)
        #         connection.commit()
        #     return "Yes"


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


