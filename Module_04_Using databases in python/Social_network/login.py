import pymysql
from easygui import *


def loginIn(connection):
    while True:
        table = multpasswordbox("Зайдіть у свій акаунт", "Table", ["Логін", "Пароль"])
        with connection.cursor() as cursor:
            login = f"select * FROM `users` where login = '{table[0]}' and parol = '{table[1]}'"
            cursor.execute(login)
            connection.commit()
            result = cursor.fetchall()
            for i in result:
                if table[0] == i["Login"] and table[1] == i["Parol"]:
                    msgbox('Ви успішно зайшли у свій акаунт', 'Welcome', 'ОК', 'images\\good.gif')
                    login = i["Login"]
                    break
                else:
                    msgbox("Невірний пороль або логін")
            break
    return login
