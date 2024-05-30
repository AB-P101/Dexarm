import pyodbc

SERVER = 'DESKTOP-DNCTOD0\TEW_SQLEXPRESS'
DATABASE = 'test_robot'
USERNAME = 'sa'
PASSWORD = '1234'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT * FROM joint_c;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)
