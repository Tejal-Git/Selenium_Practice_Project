#select
import mysql.connector
try:
    con=mysql.connector.connect(host="localhost", port="3306",user="root",password="NoAccess@240998", database="school")
    curs=con.cursor() #create cursor
    curs.execute("SELECT * FROM students") #execute query through cursor

    for row in curs:
        print(row[0],row[1],row[2],row[3],row[4])

    con.close()
except:
    print("connect unsuccessful")

print("Finished")