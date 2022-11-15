from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def add_product(request, product, price):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='12921292a',
            database="basket",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Ok")

        try:
            with connection.cursor() as cursor:
                ins = f"insert into `product` (nameProduct, price) values ('{product}', '{price}')"
                cursor.execute(ins)
                connection.commit()
        finally:
            connection.close()

    except:
        print("Error")
    return HttpResponse(f"{product} додано у базу даних")


def info_product(request, product):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='12921292a',
            database="basket",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Ok")

        try:
            with connection.cursor() as cursor:
                sel = f"select * from basket.product WHERE nameProduct = '{product}'"
                cursor.execute(sel)
                result = cursor.fetchall()
                # res_str = f"id:{result[0].get('id')}. Назва товару: {result[0].get('nameProduct')}, Ціна: {result[0].get('price')}"
                res_str = "<br>".join([f'id: {elem.get("id")}, model: {elem.get("nameProduct")}, price: {elem.get("price")}' for elem in result])
        finally:
            connection.close()

    except:
        print("Error")
    return HttpResponse(f"Опис товару: <br>{res_str}")