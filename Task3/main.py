import pymysql
from config import host, username, password, db_name, excel_filename, excel_filename2, engine
import pandas as pd


def function1(con):
    sp = []
    sp1 = []
    try:
        with con.cursor() as cur:
            print('Введите длину словаря: ')
            m = int(input())
            print('Введите значения для первого списка:')
            for _ in range(m):
                sp.append(input())
            print('Введите значения для второго списка:')
            for _ in range(m):
                sp1.append(input())

            sel = "INSERT INTO TABLE13(key_id, number) VALUES (%s, %s);"

            for i in range(m):
                val = (sp[i], sp1[i])
                cur.execute(sel, val)
            con.commit()
    finally:
        return 'COMPLETE!'


def function2(con):
    sp2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sp3 = [1, 2 ** 3, 3 ** 3, 4 ** 3, 5 ** 3, 6 ** 3, 7 ** 3, 8 ** 3, 9 ** 3, 10 ** 3]
    try:
        with con.cursor() as cur:
            sel = "INSERT INTO TABLE12(key_id, number) VALUES (%s, %s);"

            for i in range(10):
                val = (sp2[i], sp3[i])
                cur.execute(sel, val)
            con.commit()
    finally:
        return 'COMPLETE!'


def print_all(con):
    try:
        sel = "SELECT id, key_id, number FROM table13;"
        dp = pd.read_sql(sel, con=engine)
        dictionary = dict()
        for i in dp['key_id']:
            for j in dp["number"]:
                dictionary[i] = j

        sel1 = "SELECT id, key_id, number FROM table12;"
        dp1 = pd.read_sql(sel1, con=engine)
        dictionary1 = dict()
        for i in dp1['key_id']:
            for j in dp1["number"]:
                dictionary1[i] = j
    finally:
        return [dictionary, dictionary1]


def print_all_from_excel():
    try:
        workbook = pd.read_excel(excel_filename)
        data = pd.DataFrame(workbook)
        dictionary = dict()
        for i in data['key_id']:
            for j in data["number"]:
                dictionary[i] = j
        workbook2 = pd.read_excel(excel_filename2)
        data2 = pd.DataFrame(workbook2)
        dictionary1 = dict()
        for i in data2['key_id']:
            for j in data2["number"]:
                dictionary1[i] = j
    finally:
        return [dictionary, dictionary1]


def save_to_excel(con):
    try:
        sel = "SELECT id, key_id, number FROM table13;"
        dp = pd.read_sql(sel, con=engine)
        sel1 = "SELECT id, key_id, number FROM table12;"
        dp1 = pd.read_sql(sel1, con=engine)

        dp.to_excel(excel_filename, index=False)
        dp1.to_excel(excel_filename2, index=False)
    finally:
        return f'File: {excel_filename} and {excel_filename2} created!'


def clear_table1(con):
    try:
        with con.cursor() as cur:
            sel = "TRUNCATE table13;"
            cur.execute(sel)
            con.commit()
    finally:
        return 'Deleted!'


def clear_table2(con):
    try:
        with con.cursor() as cur:
            sel = "TRUNCATE table12;"
            cur.execute(sel)
            con.commit()
    finally:
        return 'Deleted!'


try:
    con = pymysql.connect(
        host=host,
        port=3306,
        user=username,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Successfully connected <3')

    flag = True
    while flag:
        print('Выберите необходимую функцию:\n'
              '   Создать первый словарь из двух списков и сохранить результаты в MySQL: 1\n'
              '   Создать второй словарь из двух списков и сохранить результаты в MySQL: 2\n'
              '   Вывести все результаты на экран из MySQL: 3\n'
              '   Сохранить все результаты в Excel: 4\n'
              '   Вывести все результаты на экран из Excel: 5   \n'
              '   Отчистить первую таблицу: #1\n'
              '   Отчистить вторую таблицу: #2\n'
              '   EXIT: 0')
        n = input()
        if n == '1':
            print(function1(con))
        elif n == '2':
            print(function2(con))
        elif n == '3':
            sp = print_all(con)
            print(sp[0])
            print(sp[1])
        elif n == '4':
            print(save_to_excel(con))
        elif n == '5':
            sp = print_all_from_excel()
            print(sp[0])
            print(sp[1])
        elif n == '#1':
            print(clear_table1(con))
        elif n == '#2':
            print(clear_table2(con))
        elif n == '0':
            flag = False
            print('EXIT!')
            con.close()
        else:
            print('Неверная команда\n'
                  'Проверте корректность вводимых данных')


except Exception as ex:
    print('Connection refused....')
    print(ex)