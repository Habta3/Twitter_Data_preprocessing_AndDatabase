import mysql.connector
from mysql.connector import Error
#create database
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='root',
                                         password='1234')

try:


    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))






try:

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                               VALUES 
                               (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")