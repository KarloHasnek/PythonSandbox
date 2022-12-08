import sqlite3

name = input("Name: ")
phone = input("Phone number: ")
email = input("Email: ")

db = sqlite3.connect('example.db')
#db.execute("create table contacts (name, phone, email)")
db.execute("insert into contacts (name, phone, email) values (?, ?, ?)", (name, phone, email))
db.commit()
db.close()
