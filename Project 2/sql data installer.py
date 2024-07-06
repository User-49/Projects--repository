import mysql.connector
sqldb = mysql.connector.connect(user='root',passwd='kapil2006@_MYSQL',host='localhost',database='Project_2_database')
csr = sqldb.cursor()
f = open('mysql_data.txt','r',encoding='UTF-8')
for i in f.readlines():
    csr.execute(i[:-1])
sqldb.commit()
