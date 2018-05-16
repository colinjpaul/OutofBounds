import sqlite3


db = sqlite3.connect('scorecard.sqlite')
cur = db.cursor()

hole = 1
par = 4
score = 5

cur.execute('''CREATE TABLE scores(Hole INT UNIQUE, Par INT, Score INT)''')

# score = input("Enter your score > ")
# print("You scored ", score)

cur.execute('''INSERT INTO scores(Hole, Par, Score)
            VALUES(?,?,?)''', (hole, par, score))

db.commit()



