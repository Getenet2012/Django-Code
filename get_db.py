import mysql.connector

myDataBase = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '',

)
cursorObject = myDataBase.cursor()
cursorObject.execute("CREATE DATABASE getnet_db")
print("All Done!")