import sqlite3
from logpas import x

base = sqlite3.connect("nnnew.db")
cur = base.cursor()
#base.execute("CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY,password)".format("data"))
#base.commit()

#cur.execute("INSERT INTO data VALUES(?, ?)",("JONNY133","123456789"))
#base.commit()
#cur.execute("INSERT INTO data VALUES(?, ?)",("biily123","passwort"))
#base.commit()
#cur.executemany("INSERT INTO data VALUES(?, ?)",(x))
#base.commit()
#cur.execute("INSERT INTO data VALUES(?, ?)",("JONNY134","1234567890"))
#base.commit()'''
r = cur.execute("SELECT password FROM data").fetchall()
print(r)
r = cur.execute("SELECT password FROM data WHERE login == ?",("JONNY133",)).fetchone()
print(r)
cur.execute("UPDATE data SET password == ? WHERE password == ?",("passwort55","passwort"))
base.commit()
cur.execute("DELETE FROM data  WHERE login==?",("JONNY133",))
base.commit()

#base.execute("DROP TABLE IF EXISTS data")
base.commit()
base.close()


