import pymysql
from easygui import *
from login import *
from add_data import *
from filestart import *



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
        log_now = 0
        choice = 0
        while choice != "Відміна":
            choice = buttonbox("SocialNetwork", "Authorizationr", ["Авторизація", "Відміна"], 'images\\j.gif')
            if choice == "Авторизація":
                log_now = loginIn(connection)
                if log_now in alllogin(connection):
                    while choice != "Відміна":
                        choice = buttonbox("Подальші дії", "Social network",
                                           ["Settings", "Search", "Friends",
                                            "Posts", "User info",
                                            "Відміна"], 'images\\1.gif')
                        if choice == "User info":
                            selectAllFromUser(connection, log_now)
                        if choice == "Search":
                            findUser(connection)
                        if choice == "Posts":
                            while choice != "Повернутись":
                                choice = buttonbox("Подальші дії", "Social network",
                                                   ["Додати пост", "Перегляд усіх публікацій", "Видалити пост",
                                                    "Повернутись"], 'images\\post.gif')
                                if choice == "Додати пост":
                                    addPost(connection, log_now)
                                if choice == "Перегляд усіх публікацій":
                                    allPosts(connection, log_now)
                                if choice == "Видалити пост":
                                    delPost(connection, log_now)
                        if choice == "Friends":
                            while choice != "Повернутись":
                                choice = buttonbox("Подальші дії", "Social network",
                                                   ["Додати друга", "Переглянути друзів", "Видалити друга", "Повернутись"],
                                                   'images\\fr.gif')
                                if choice == "Додати друга":
                                    addFriend(connection, log_now)
                                if choice == "Переглянути друзів":
                                    allFriend(connection, log_now)
                                if choice == "Видалити друга":
                                    delFriend(connection, log_now)
                        if choice == "Settings":
                            while choice != "Повернутись":
                                choice = buttonbox("Подальші дії", "Social network",
                                                   ["Реєстрація нового юзера", "Видалити акаунт",
                                                    "Редагувати інформацію", "Повернутись"], 'images\\set.gif')
                                if choice == "Реєстрація нового юзера":
                                    addUser(connection)
                                if choice == "Видалити акаунт":
                                    delUser(connection, log_now)
                                    break
                                if choice == "Редагувати інформацію":
                                    editInfoFromUser(connection, log_now)
                else:
                    break
    finally:
        connection.close()

except:
    print("Error")
