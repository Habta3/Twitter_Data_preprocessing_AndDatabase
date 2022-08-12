import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='TweetDatabase',
                                         user='root',
                                         password='1234')

    sql_select_Query = "select * from TweetInformation"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
        print("Id = ", row[4], )
        print("Name = ", row[5])
        print("Price  = ", row[6])
        print("Purchase date  = ", row[7], "\n")
        print("Id = ", row[8], )
        print("Name = ", row[9])
        print("Price  = ", row[10])
        print("Purchase date  = ", row[11], "\n")
        print("Id = ", row[12], )
        print("Name = ", row[12])
        print("Price  = ", row[14])


except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")