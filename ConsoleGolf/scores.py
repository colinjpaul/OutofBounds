import sqlite3
import os
import pandas as pd

home = os.path.dirname("C:/Users/cpaul/Documents/GitHub/OutofBounds/Data/")
abs_file_path = os.path.join(home, "Scorecard.csv")
#
df = pd.read_csv(abs_file_path)

db = sqlite3.connect('scorecard.sqlite')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS scores(Hole INT UNIQUE, Par INT, Score INT)''')

print("new changes from branch 7")


# cur.execute('''INSERT INTO scores(Hole, Par, Score)
#             VALUES(?,?,?)''', (hole, par, score))
#
# cur.execute('''SELECT hole, par, score FROM scores''')
# # one_hole = cur.fetchone()
# # print(one_hole[2])
# all_rows = cur.fetchall()
# for row in all_rows:
#     print('Hole: {0}, Par: {1}, Score: {2} '.format(row[0], row[1], row[2]))






