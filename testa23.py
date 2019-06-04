import psycopg2
connection=psycopg2.connect(user='test',password="36network",host="127.0.0.1",port="5432",database="employee")
cursor=connection.cursor()
print(connection.get_dsn_parameters(),"\n")
cursor.execute("SELECT * from employee")
record=cursor.fetchall()
print("printing record")
print(record)
