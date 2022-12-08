import sqlite3
import socket

#for_ratings
db = sqlite3.connect('example2.db')
db.execute("create table ratings (hostname, rating)")
hostname = socket.gethostname()
user_experience = input("Rate your experience: ")

if user_experience:
    db.execute("insert into Ratings (hostname, rating) values (?, ?)", (hostname, user_experience))
    db.commit()
    db.close()
    print("Thank you for your rating :)")
else:
    print("User input invalid. Please try again.")
