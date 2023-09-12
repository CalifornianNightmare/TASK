import pymysql
from config import host, username, password, db_name


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

    a, b = int(input()), int(input())
    val = a+b

    try:
        with con.cursor() as cur:
            sel = "INSERT INTO TABLE1 (comb) VALUES (%s);"
            cur.execute(sel, val)
            con.commit()
            print('Lypa')
    finally:
        con.close()

except Exception as ex:
    print('Connection refused....')
    print(ex)
