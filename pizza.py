import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="foods")

mycursor = mydb.cursor()

mycursor.execute("DELETE DATABASE foods")

mydb.commit()

