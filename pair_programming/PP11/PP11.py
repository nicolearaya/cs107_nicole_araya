# Ben Manning
# Nicole Araya
# Qinyi Chen

import sqlite3


db = sqlite3.connect('candidates.sqlite')
cursor = db.cursor() # https://www.python.org/dev/peps/pep-0249/#cursor-objects
cursor.execute("DROP TABLE IF EXISTS candidates") # Convenient in case you want to start over

cursor.execute('''CREATE TABLE candidates (
               id TEXT, 
               first_name TEXT, 
               last_name TEXT, 
               middle_name TEXT, 
               party TEXT NOT NULL)''')

db.commit() # Commit changes to the database

a_file = open("candidates.txt", "r")
candidates = []
lines = a_file.readlines()
for line in lines[1:]:
    line = line.strip('\n')
    line = tuple(line.split('|'))
    candidates.append(line)

cursor.executemany('INSERT INTO candidates (id, first_name, last_name, middle_name, party) VALUES (?, ?, ?, ?, ?)', candidates)
db.commit()


cursor.execute("SELECT * FROM candidates")
all_rows = cursor.fetchall()
print(all_rows)