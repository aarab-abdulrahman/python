import tkinter 
import sqlite3
from tkinter import messagebox
from ttkbootstrap import ttk , style , Label
import ttkbootstrap as tb
from PIL import Image, ImageTk
import json


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
         
        if button_states['button2']==True:
            entry_url.delete(0,tkinter.END)
            entry_username.delete(0,tkinter.END)
            entry_password.delete(0,tkinter.END)   
        else:
            pass
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


# ______________________page2__________________


def toggle_button(buttonx_name):
    global button_states
    if button_states[buttonx_name]:
        button_states[buttonx_name]=False
        save_setting()
        return True
    else:
        button_states[buttonx_name]=True
        save_setting()
        return False 

def off_on_button1(button_name,txt,x,entry1,entry2,style):
    button_name.config(text=txt,bootstyle=style)
    entry1.config(show=x)
    entry2.config(show=x)

def button1_execut():
    if toggle_button('button1'):
        off_on_button1(button1,'OFF',"",entry_url,entry_username,"danger")
    else:
        off_on_button1(button1,'ON',"*",entry_url,entry_username,"success")

def button2_execut():
    if toggle_button('button2'):
        button2.config(text="OFF",bootstyle="danger")
    else:
        button2.config(text="ON",bootstyle="success")

    
    
# _________json___________

SETTINGS_FILE="settings.json"
def save_setting():
    global button_states     
    with open(SETTINGS_FILE,mode="w") as file:
        json.dump(button_states,file)

def load_settings():
    global button_states
    try:
        with open (SETTINGS_FILE,mode="r") as file:
            button_states=json.load(file)
    except:
        pass

def on_close():
    save_setting()
    root.destroy()

button_states={
    'button1':False,
    'button2':False,
}
load_settings()

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
    text="Home",
    command=lambda: show_page("page1"),
    bootstyle="danger-link"
)
btn_page1.pack(side="left", padx=10, pady=5)

btn_page2 = ttk.Button(
    navbar_frame,
    text="Settings",
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
    # highlightthickness=2,
    # highlightbackground="#eb0722",
    # highlightcolor="#57eb07"
    
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

# Page 2 (Settings )
page2 = ttk.Frame(root,bootstyle="cyborg")
pages['page2'] = page2
# ttk.Label(page2, text="Page 2 - Settings or Additional Features").pack(pady=10)


label_noothing=ttk.Label(
    page2,
    text=""
)
label_noothing.grid(row=0,column=2,padx=160)

# ______________________________

label1=Label(
    page2,
    text="Hide text",
    # background="#ffcccc",  
    foreground="white",  
    font=12
)
label1.grid(row=1,column=2)



button1=ttk.Button(
    page2,
    text="OFF",
    command=button1_execut,
    bootstyle='danger',
)

if button_states['button1']:
  off_on_button1(button1,'ON',"*",entry_url,entry_username,"success")


button1.grid(row=1,column=3)

# ______________________________
label2=Label(
    page2,
    text="Delete text (after completion)",
    font=12
)
label2.grid(row=2,column=2,pady=25)

button2=ttk.Button(
    page2,
    text="OFF",
    command=button2_execut,
    bootstyle='danger',
)
if button_states['button2']:
    button2.config(text="ON",bootstyle="success")

button2.grid(row=2,column=3)


# _____________
frameh=ttk.Frame(page2,height=1,style="light")
framev=ttk.Frame(page2,width=1,style="light")
# _______________
fh1=frameh
fv2=framev
fh1.place(relwidth=1,y=60)
fv2.place(relheight=1,x=300)


# Show the default page__
show_page('page1')

root.protocol("WM_DELETE_WINDOW",on_close)
root.mainloop()
