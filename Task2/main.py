import pymysql
import pandas as pd
from config import host, username, password, db_name, engine, excel_filename


def function1(a, b, c, con):
    sp = []
    try:
        with con.cursor() as cur:
            sel = "INSERT INTO TABLE12 (number) VALUES (%s);"
            sp.append(a + b)
            sp.append(a - b)
            sp.append(a * b)
            sp.append(a / b)
            sp.append(a // b)
            sp.append(a % b)
            sp.append(a ** b)
            sp.append((a ** b) % c)
            for val in sp:
                cur.execute(sel, val)
            con.commit()
    finally:
        return 'COMPLETE!'


def clear_table(con):
    try:
        with con.cursor() as cur:
            sel = "TRUNCATE table12;"
            cur.execute(sel)
            con.commit()
    finally:
        return 'Deleted!'


def print_all(con):
    try:
        sel = "SELECT * FROM table12;"
        dp = pd.read_sql(sel, con=engine)

    finally:
        return dp


def save_all_to_excel(con):
    try:
        sel = "SELECT * FROM table12;"
        dp = pd.read_sql(sel, con=engine)
        dp.to_excel(excel_filename, index=False)
    finally:
        return 'COMPLETE!'


def print_all_from_excel():
    try:
        workbook = pd.read_excel(excel_filename)
        data = pd.DataFrame(workbook)
    finally:
        return data


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
            '    Ввести числа с клавиатуры, произвести арифметические вычисления и сохранить результат в MySQL: 1\n'
            '    Вывести все результаты на экран из MySQL: 2\n'
            '    Сохранить все результаты в Excel: 3\n'
            '    Вывести все результаты на экран из Excel: 4 \n'
            '    Отчистить таблицу: #1\n'
            '    EXIT: 0')
        n = input()
        if n == '1':
            a, b, c = float(input("A: ")), float(input('B: ')), float(input('Модуль: '))
            print(function1(a, b, c, con))
        elif n == '2':
            print(print_all(con))
        elif n == '3':
            print(save_all_to_excel(con))
        elif n == '4':
            print(print_all_from_excel())
        elif n == '#1':
            print(clear_table(con))
        elif n == '0':
            flag = False
            print('Bye, bye!')
            con.close()
        else:
            print('Неверная команда\n'
                  'Проверте корректность вводимых данных')
except Exception as ex:
    print('Connection refused....')
    print(ex)
