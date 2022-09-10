import mysql.connector
#importing database
database = mysql.connector.connect(
host="localhost",
user="root",
password=""
)
db = database.cursor()

db.execute("CREATE DATABASE pythons")

import mysql.connector
#importing database
database = mysql.connector.connect(
host="localhost",
user="root",
password="",
database = "class4pm"
)
db = database.cursor()

db.execute("SELECT * FROM student")
result =db.fetchall()
for data in result:
    print(data)

db.execute("SELECT * FROM student WHERE name = 'Hari'")
result =db.fetchall()
for data in result:
    print(data)

db.execute("SELECT * FROM student WHERE total > 410")
result =db.fetchall()
for data in result:
    print(data)

db.execute("SELECT sn, name, total, per, grade FROM student")
result =db.fetchall()
for data in result:
    print(data)

sql = '''INSERT INTO `student` ( `name`, `physics`, `chemistry`, `math`, `english`, `nepali`, `total`, `per`, `grade`) 
VALUES ( 'ram Prasad', '56', '67', '67', '91', '67', '378', '72.5', 'B')'''
db.execute(sql)
database.commit()

n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    physics = int(input("Enter physics marks = "))
    chemistry = int(input("Enter chemistry marks = "))
    math = int(input("Enter math marks = "))
    english = int(input("Enter english marks = "))
    nepali = int(input("Enter nepali marks = "))
    total = sum([physics,chemistry,math,english,nepali])
    per = total/5
    if per>=80:
        grade = 'A'
    elif per>=60:
        grade = 'B'
    elif per>=45:
        grade = 'C'
    else:
        grade = 'F'
        
    sql = f'''INSERT INTO student ( name, physics, chemistry, math, english, nepali, total, per, grade) 
    VALUES ( '{name}',{physics} , {chemistry}, {math}, {english}, {nepali}, {total}, {per}, '{grade}')'''
    print(sql)
    db.execute(sql)
    
database.commit()

# Delete
sql = "DELETE FROM student WHERE sn = 5"
db.execute(sql)
database.commit()

ids = int(input("Enter id = "))
sql = f"DELETE FROM student WHERE sn = {ids}"
db.execute(sql)
database.commit()

# Update
sql = "UPDATE student SET name = 'Nabina' WHERE name = 'Nabin'"
db.execute(sql)
database.commit()

# Update
sql = "UPDATE student SET name = 'Nabina' WHERE name = 'Nabin' and grade = 'A'"
db.execute(sql)
database.commit()