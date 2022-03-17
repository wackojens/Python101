import mysql.connector
from dotenv import dotenv_values
from mysql.connector import Error

config = dotenv_values(".env")

try:
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        cursor = conn.cursor()
        klantnr = input("Geef een klantnr in:")
        strSQL = "select * from customers where customerNumber = %(klantnr)s"
        cursor.execute(strSQL,{'klantnr':klantnr})
        records = cursor.fetchall()
        for record in records:
            print(record)
except Error as e:
    print("Error connectie met MySQL", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Het MySQL connectie object is gesloten")




""" volgende code stond origineel ook in de try: if:
print("De connectie met de MySQL Server is gelukt.")
serverInfo = conn.get_server_info()
print("Connectie met MySQL Server versie", serverInfo)
cursor = conn.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("Verbinding met de database:", record)"""


