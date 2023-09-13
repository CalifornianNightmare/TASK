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

    try:
        with con.cursor() as cur:
            sel = "TRUNCATE table13;"
            cur.execute(sel)
            con.commit()
            print('Deleted!')
    finally:
        con.close()

except Exception as ex:
    print('Connection refused....')
    print(ex)