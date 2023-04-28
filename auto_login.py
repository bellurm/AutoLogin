from tkinter import *
from tkinter import messagebox
import queries, requests, time
import webbrowser as web
import pyautogui as pg
import pyperclip as pc

def send_data_to_queries():
	url = loginUrlEntry_db.get()
	username = usernameEntry_db.get()
	password = passwordEntry_db.get()
	queries.addRecord(url, username, password)

def refreshListbox():
    list_of_records.delete(0, END)
    showRecords = queries.showRecords()
    for rowRecords in enumerate(showRecords, 1):
	    list_of_records.insert(END, rowRecords)

def delete_selected_item():
    selected_item_index = list_of_records.curselection()
    if selected_item_index:
        selected_item = list_of_records.get(selected_item_index)
        queries.deleteRecord(selected_item[1][0])

def login():
    selected_item_index = list_of_records.curselection()
    if selected_item_index:
        selected_item = list_of_records.get(selected_item_index)
        url = selected_item[1][0]
        username = selected_item[1][1]
        password = selected_item[1][2]
        userAgent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        requests.get(url, headers=userAgent)
        time.sleep(1)
        web.open(url)
        time.sleep(10)
        pc.copy(username)
        pg.hotkey("ctrl", "v")
        pg.hotkey("TAB")
        time.sleep(1)
        pc.copy(password)
        pg.hotkey("ctrl", "v")
        pg.press("Enter")

root = Tk()
messagebox.showinfo("IMPORTANT", "If you want to go to a website, you have to click one time to the site's username area.")
root.geometry("1000x700")
root.title("Cyber Worm - Auto Login")
root.configure(bg="#005b96")


addDatabaseFrame = LabelFrame(root, text="Add a website.", fg="red", bg="#005b96", font=('Arial', 15, 'bold'), height=300, width=950)
addDatabaseFrame.place(relx=0.01, rely=0.01)

loginUrlLabel_db = Label(addDatabaseFrame, text="Login Page URL:", bg="#005b96", fg="white", font=('Arial', 14, 'bold'))
loginUrlLabel_db.place(relx=0.3, rely=0.1)

loginUrlEntry_db = Entry(addDatabaseFrame, width=30, border=5)
loginUrlEntry_db.place(relx=0.5, rely=0.1)

usernameLabel_db = Label(addDatabaseFrame, text="Username:", bg="#005b96", fg="white", font=('Arial', 14, 'bold'))
usernameLabel_db.place(relx=0.3, rely=0.3)

usernameEntry_db = Entry(addDatabaseFrame, width=30, border=5)
usernameEntry_db.place(relx=0.5, rely=0.3)

passwordLabel_db = Label(addDatabaseFrame, text="Password:", bg="#005b96", fg="white", font=('Arial', 14, 'bold'))
passwordLabel_db.place(relx=0.3, rely=0.5)

passwordEntry_db = Entry(addDatabaseFrame, width=30, border=5)
passwordEntry_db.place(relx=0.5, rely=0.5)

add_to_Database_Button = Button(addDatabaseFrame, text="Add to Database", fg="#005b96", font=('Arial', 14, 'bold'), width=35, height=2, command=send_data_to_queries)
add_to_Database_Button.place(relx=0.05, rely=0.75)

showRecordsFrame = LabelFrame(root, text="Records.", fg="red", bg="#005b96", font=('Arial', 15, 'bold'), height=300, width=920)
showRecordsFrame.place(relx=0.01, rely=0.5)

scrbar = Scrollbar(showRecordsFrame)
scrbar.pack(side=RIGHT, fill=Y)
list_of_records = Listbox(showRecordsFrame, yscrollcommand=scrbar.set, width=85, height=10, bg='#005b96', fg='white', font=('Arial', 15, 'bold'))
list_of_records.pack(side=LEFT)
scrbar.config(command=list_of_records.yview)

goButton = Button(root, text="Go to selected website.", fg="#005b96", font=('Arial', 14, 'bold'), width=35, height=2, command=login)
goButton.place(relx=0.5, rely=0.91)

refreshButton = Button(root, text="Refresh", fg="#005b96", font=('Arial', 14, 'bold'), width=35, height=2, command=refreshListbox)
refreshButton.place(relx=0.05, rely=0.91)

delete_from_Database_Button = Button(addDatabaseFrame, text="Delete from Database", fg="#005b96", font=('Arial', 14, 'bold'), width=35, height=2, command=delete_selected_item)
delete_from_Database_Button.place(relx=0.5, rely=0.75)

refreshListbox()
root.mainloop()
