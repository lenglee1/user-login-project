import hashlib
import sqlite3
import os
import getpass


path = "/Users/lenglee/Documents/python_playfiles/projectEuler/loginProject"
os.chdir(path)

con = sqlite3.connect('ppab6.db')
cur = con.cursor()


#Define functions to ask for username and to hash a password

def ask_username():
	username = input("What is your username?")
	return username


def hash_password(password):
	encoded_password = password.encode()
	h_password = hashlib.sha256(encoded_password).hexdigest()	
	return h_password

#Ask for username

username = ask_username()

#Ask for password

try:
	password = getpass.getpass(prompt = 'Please enter a password: ')
except Exception as E:
	print('There is an Error : ', E)
# else:
# 	print('Password fetched from command prompt :', password)

hashed_password = hash_password(password)

#print(username, hashed_password)
# print("Username is {uname} and password is {pword}".format(uname = username, pword = password))	

#Check if username exists in DB

def check_unique_username(username):
	cur.execute("SELECT username FROM users WHERE username = (?)", (username,))
	data = cur.fetchall()
	if len(data) == 0:
		return True
	else:
		return False

def add_new_user(username, hashed_password):
	cur.execute("INSERT INTO users VALUES (?,?)", (username, hashed_password,))
	con.commit()


def validate_credential(username, hashed_password):
	cur.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, hashed_password,))
	data = cur.fetchall()

	if len(data) == 1:
		print("Credentials validated. Enjoy the site")
	else:
		print("Please check your username and password")

def print_all_users():
	cur.execute("SELECT * FROM users")
	rows = cur.fetchall()

	for row in rows:
		print(row)

#Validate username - let them in or create new user

if check_unique_username(username) == True:
	add_new_user(username, hashed_password)
	print("Welcome new user!")
else:
	validate_credential(username, hashed_password)
	
print_all_users()


con.close()
exit()

