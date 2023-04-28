import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("records.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS siteRecords(url TEXT, username TEXT, passwd TEXT)")
connection.commit()

def showRecords():
	cursor.execute("SELECT * FROM siteRecords")
	return cursor.fetchall()

def addRecord(url, username, password):
	query = (f"INSERT INTO siteRecords VALUES('{url}', '{username}', '{password}')")
	cursor.execute(query)
	connection.commit()
	messagebox.showinfo("Transaction INFO", "Success.")

def deleteRecord(url):
	query = f"DELETE FROM siteRecords WHERE url='{url}'"
	cursor.execute(query)
	connection.commit()
	messagebox.showinfo("Transaction INFO", "Success.")

