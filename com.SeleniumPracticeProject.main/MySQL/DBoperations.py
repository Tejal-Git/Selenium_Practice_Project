# insert, update, delete

#insert
import mysql.connector

# con=mysql.connector.connect(host="localhost", port="3306",user="root",password="NoAccess@240998", database="school")
# curs=con.cursor() #create cursor
# curs.execute("INSERT INTO students (name, age, grade, email) VALUES('Hannah paul', 15, 'B', 'hannah.paul@email.com')") #execute query through cursor
# con.commit() #commit transaction
# con.close()
#
# print("Finished")

#update
# con=mysql.connector.connect(host="localhost", port="3306",user="root",password="NoAccess@240998", database="school")
# curs=con.cursor() #create cursor
# curs.execute("UPDATE students SET grade = 'A+'WHERE name = 'John Doe';") #execute query through cursor
# con.commit() #commit transaction
# con.close()
#
# print("Finished")

#delete
con=mysql.connector.connect(host="localhost", port="3306",user="root",password="NoAccess@240998", database="school")
curs=con.cursor() #create cursor
curs.execute("DELETE FROM students WHERE email = 'bob.johnson@email.com'") #execute query through cursor
con.commit() #commit transaction
con.close()

print("Finished")