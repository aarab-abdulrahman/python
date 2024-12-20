import sqlite3
from rich.console import Console
import time

class User():
    def __init__ (self,idx,name,gend,city,email,phone):

        self.idx=id(self)
        self.name=name
        self.gend=gend
        self.city=city
        self.email=email
        self.phone=phone

        # _____data
        self.connect=sqlite3.connect('user_details.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS user(
                    id INTEGET,
                    name TEXT ,
                    gend TEXT,
                    city TEXT,
                    email TEXT,
                    phone INTEGET PRIMARY KEY,    
                            )
                            ''')
        self.connect.commit()

        self.cursor.execute("INSERT INTO user (id,name,gend,city,email,phone) VALUES (?,?,?,?,?,?)",(self.idx,self.name,self.gend,self.city,self.email,self.phone))
        self.connect.commit()

        self.connect.close()


class Login:
    def __init__(self,your_name):
        self.id=id(self)
        self.name=your_name

        # __data
        self.connect=sqlite3.connect('login.db')
        self.cursor=self.connect.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS login(
                name TEXT PRIMARY KEY          
                            )
                            ''')
        self.connect.commit()
    def insert(self):
        self.cursor.execute('INSERT INTO login (name) VALUES (?)',(self.name,))
        self.connect.commit()

    def is_exist():
        connect=sqlite3.connect('login.db')
        cursor=connect.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS login(
                name TEXT PRIMARY KEY       
                       )
         ''')
        connect.commit()

        cursor.execute('SELECT * FROM login')
        result =cursor.fetchall()
        connect.close()

        return result
        


def effect_write(text,name_color="white",delay=0.1):
    for i in text: 
        Console().print(f'[{name_color}]{i}[/{name_color}]',end="",style="bold")
        time.sleep(delay)



# ____________________________________________

if Login.is_exist():
    name_fetch=Login.is_exist()[0][0]
    effect_write(f"Welcome back , {name_fetch}!\n","blue")
else:
    your_name=input('type your name : ').strip().capitalize()
    new_login=Login(your_name)
    new_login.insert()
    effect_write(f"Welcome , {your_name}!\n","green")



















