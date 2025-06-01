import sqlite3

con = sqlite3.connect('app.db')
with open('database/schema.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)