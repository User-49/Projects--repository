import mysql.connector
sqldb = mysql.connector.connect(user='root',passwd='kapil2006@_MYSQL',host='localhost')
csr = sqldb.cursor()
f = open('D:\projects\Projects--repository\Project 3\mysql_data.txt','r',encoding='UTF-8')
for i in f.readlines():
    csr.execute(i[:-1])
sqldb.commit()
