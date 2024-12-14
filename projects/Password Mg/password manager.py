import tkinter 
import sqlite3
from tkinter import messagebox
from ttkbootstrap import ttk
import ttkbootstrap as tb
from PIL import Image, ImageTk


def creat_datab():
    connect = sqlite3.connect("password_manager.db")
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords_manager
                      (url TEXT PRIMARY KEY, email_username TEXT, password TEXT)''')
    connect.commit()
    connect.close()


def save_password():
    url = entry_url.get()
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "" or url == "":
        messagebox.showwarning('Error', 'Please type username/email, URL, and password.')
        return

    connect = sqlite3.connect('password_manager.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM passwords_manager WHERE url=?', (url,))
    result = cursor.fetchone()

    if result:
        messagebox.showwarning('Error', f'This URL "{url[:10]}..." already exists.')
    else:
        cursor.execute('INSERT INTO passwords_manager (url, email_username, password) VALUES (?, ?, ?)',
                       (url, username, password))
        connect.commit()
        messagebox.showinfo('Success', 'Password saved successfully!')

    connect.close()


def view_password():
    connect = sqlite3.connect('password_manager.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM passwords_manager')
    rows = cursor.fetchall()

    if not rows:
        messagebox.showinfo('Search', 'No data found.')
    else:
        result_window = tkinter.Toplevel(root)
        result_window.title('Saved Passwords')

        tree = ttk.Treeview(result_window, columns=('url', 'email_username', 'password'), show="headings")
        tree.heading("url", text="URL")
        tree.heading('email_username', text="Username / Email")
        tree.heading('password', text="Password")

        for row in rows:
            tree.insert('', tkinter.END, values=row)
        tree.pack(padx=10, pady=10)

    connect.close()


def checker():
    if var1.get() == 0:
        entry_password.config(show="")
    else:
        entry_password.config(show="*")


def show_page(page):
    for frame in pages.values():
        frame.pack_forget()
    pages[page].pack(fill="both", expand=True)


# Main application
root = tb.Window(themename="darkly")
root.title('Password Manager')
root.geometry('400x400')
icon_image = Image.open("password_key_18843.ico")
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)
root.resizable(False, False)

# Create the database
creat_datab()

# Navigation bar
navbar_frame = ttk.Frame(root, bootstyle="cyborg")
navbar_frame.pack(side="top", fill="x")

btn_page1 = ttk.Button(
    navbar_frame,
    text="Page 1",
    command=lambda: show_page("page1"),
    bootstyle="danger-link"
)
btn_page1.pack(side="left", padx=10, pady=5)

btn_page2 = ttk.Button(
    navbar_frame,
    text="Page 2",
    command=lambda: show_page("page2"),
    bootstyle="success-link"
)
btn_page2.pack(side="right", padx=10, pady=5 )

# Pages setup
pages = {}

# Page 1 (Password Management)
page1 = ttk.Frame(root,bootstyle="cyborg",)
pages["page1"] = page1

label_url = ttk.Label(
    page1,
    text="URL",
)
label_url.grid(row=0, column=2, pady=10, padx=200)

entry_url = ttk.Entry(
    page1,
    width=30,
)
entry_url.grid(row=1, column=2)

label_username = ttk.Label(
    page1,
    text="Username / Email"
)
label_username.grid(row=2, column=2, pady=10)

entry_username = ttk.Entry(
    page1,
    width=30,
)
entry_username.grid(row=3, column=2)

label_password = ttk.Label(
    page1,
    text="Password",
)
label_password.grid(row=4, column=2, pady=10)

entry_password = ttk.Entry(
    page1,
    width=30,
    bootstyle="danger",
)
entry_password.grid(row=5, column=2)

save_button = ttk.Button(
    page1,
    text="Save",
    command=save_password,
    bootstyle=("SUCCESS", "OUTLINE"),
)
save_button.place(x=265, y=230)

view_button = ttk.Button(
    page1,
    text="View My Passwords",
    command=view_password
)
view_button.place(x=100, y=230)

var1 = tkinter.BooleanVar()
check1 = ttk.Checkbutton(
    page1,
    bootstyle="success, round-toggle",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker,
)
check1.place(x=250, y=153)

# Page 2 (Settings or Additional Features)
page2 = ttk.Frame(root,bootstyle="cyborg")
pages['page2'] = page2
ttk.Label(page2, text="Page 2 - Settings or Additional Features").pack(pady=10)

# Show the default page
show_page('page1')

root.mainloop()
