import tkinter 
import sqlite3
from tkinter import messagebox
from ttkbootstrap import ttk

def creat_datab():
    connect=sqlite3.connect("password_manager.db")
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords_manager
                      (url TEXT PRIMARY KEY , email_username TEXT , password TEXT)
                   ''')
    connect.commit()
    connect.close()

def save_password():
    url=entry_url.get()
    username=entry_username.get()
    password=entry_password.get()

    if username == "" or password=="" or url == "":
        messagebox.showwarning('error','please type username/email + url + password')
        return
    
    connect=sqlite3.connect('password_manager.db')
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM passwords_manager WHERE url=?',(url,))
    result=cursor.fetchone()

    if result:
        messagebox.showwarning('error',f'this url {url[:10]}... already exist')
    else:
        cursor.execute('INSERT INTO passwords_manager (url,email_username,password) VALUES (?,?,?)',(url,username,password))
        connect.commit()
        messagebox.showinfo('save','successfully')

    connect.close()


def view_password():
    connect=sqlite3.connect('password_manager.db')
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM passwords_manager')
    rows =cursor.fetchall()

    if not rows:
        messagebox.showinfo('search','No data entered')
    else:
        result_window=tkinter.Toplevel(root)
        result_window.title('your data')

        tree=ttk.Treeview(result_window,columns=('url','email_username','password'),show="headings")
        tree.heading("url",text="url")
        tree.heading('email_username',text="username / email")
        tree.heading('password',text="passsword")

        for row in rows:
            tree.insert('',tkinter.END , values=row)
        tree.pack(padx=10,pady=10)
    connect.close()


root=tkinter.Tk()
root.title('Password Manager')
root.geometry('400x400')

creat_datab()


# ________________________________________
label_url=ttk.Label(
    root,
    text="url",
)
label_url.grid(row=0,column=2,pady=10,padx=200)

entry_url=ttk.Entry(
    root,
    width=30,
)
entry_url.grid(row=1,column=2)

# _______________________________
label_username=ttk.Label(
    root,
    text="username"
)
label_username.grid(row=2,column=2,pady=10)

entry_username=ttk.Entry(
    root,
    width=30,
)
entry_username.grid(row=3,column=2)

# ___________________
label_password=ttk.Label(
    root,
    text="password",
    bootstyle="success",
)
label_password.grid(row=4,column=2,pady=10)

entry_password=ttk.Entry(
    root,
    width=30,
    bootstyle="success"
)
entry_password.grid(row=5,column=2)


# ______________________________
save_button=ttk.Button(
    root,
    text="save",
    command=save_password
)

view_button=ttk.Button(
    root,
    text="view my passwords",
    command=view_password
)

save_button.place(x=265,y=230)
view_button.place(x=100,y=230)

root.mainloop()