import mysql.connector
sqldb=mysql.connector.connect(host="localhost",user="kapil",paswd="kapil2006@_MYSQL");
csr=sqldb.cursor()
try:
    csr.execute("use p")