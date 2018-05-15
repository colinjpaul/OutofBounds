import sqlite3
conn = sqlite3.connect('scorecard.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS scores
    (id INT PRIMARY KEY, Hole INT UNIQUE, Par INT, 
    Handicap INT UNIQUE, Score INT)''')

score = input("Enter your score > ")
print("You scored ", score)

ins = 'INSERT INTO scores (Score) VALUES(?)'
cur.execute(ins, (5))

