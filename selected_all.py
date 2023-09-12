import pymysql
import pandas as pd
from sqlalchemy import create_engine

from config import host, username, password, db_name, excel_filename


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

    try:
        engine = create_engine(f"mysql+pymysql://root:{password}@localhost/{db_name}")
        sel = "SELECT id, comb FROM table1;"
        dp = pd.read_sql(sel, con=engine)
        print(dp)
        dp.to_excel(excel_filename, index=False)

        workbook = pd.read_excel(excel_filename)
        data = pd.DataFrame(workbook)
        print(data)



    finally:
        con.close()

except Exception as ex:
    print('Connection refused....')
    print(ex)