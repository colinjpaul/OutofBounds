import sqlite3


db = sqlite3.connect('scorecard.sqlite')
cur = db.cursor()

hole = 2
par = 3
score = 4

cur.execute('''CREATE TABLE IF NOT EXISTS scores(Hole INT UNIQUE, Par INT, Score INT)''')

# score = input("Enter your score > ")
# print("You scored ", score)

# cur.execute('''INSERT INTO scores(Hole, Par, Score)
#             VALUES(?,?,?)''', (hole, par, score))



cur.execute('''SELECT hole, par, score FROM scores''')
# one_hole = cur.fetchone()
# print(one_hole[2])
all_rows = cur.fetchall()
for row in all_rows:
    print('Hole: {0}, Par: {1}, Score: {2} '.format(row[0], row[1], row[2]))






