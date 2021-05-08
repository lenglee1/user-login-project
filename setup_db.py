import sqlite3


con = sqlite3.connect('ppab6.db')
cur = con.cursor()

cur.execute("""
	CREATE TABLE IF NOT EXISTS users (
	username VARCHAR,
	password_hash VARCHAR)
""")

users_dict = {
	'robert': ("robert", "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"), 
	'anoosh': ("anoosh", "3c32608fd9ffd87ae17dbb3a65a509cc8ba5aa395147c99ed20bdba9c434d8c2"),
	'juan':  ("juan", "5dc7286295def318e3e643b21ec8963fe1a0d4c43c0e62a7477ad43c4a04406e"), 
	'leng':  ("leng", "4b6e4d1f4b42ea34914e263d0f57ada6015f1f04306989ccaad39a4f1b25337a")
}

for name in users_dict:
	cur.execute("INSERT INTO users VALUES (?,?)", users_dict[name])

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
	print(row)

con.commit()
con.close()

print("success")

