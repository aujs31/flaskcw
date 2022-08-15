import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root" , passwd = "123123", auth_plugin='mysql_native_password')

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)