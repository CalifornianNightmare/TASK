import pymysql
from config import host, username, password, db_name


sp = []

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
    print('\n')

    a, b = float(input()), float(input())
    sp.append(a+b)
    sp.append(a-b)
    sp.append(a*b)
    sp.append(a/b)
    sp.append(a//b)
    sp.append(a%b)
    sp.append(a**b)
    sp.append((a**b) % 3)

    try:
        with con.cursor() as cur:
            sel = "INSERT INTO TABLE13 (comb) VALUES (%s);"
            for val in sp:
                cur.execute(sel, val)
            con.commit()
            print('Lypa')
    finally:
        con.close()

except Exception as ex:
    print('Connection refused....')
    print(ex)