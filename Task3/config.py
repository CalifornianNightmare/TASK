from sqlalchemy import create_engine

host = 'localhost'
username = 'root'
password = 'NeforMAL_768'
db_name = 'testdb13'
excel_filename = 'test.xlsx'
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{db_name}")
excel_filename2 = 'test2.xlsx'