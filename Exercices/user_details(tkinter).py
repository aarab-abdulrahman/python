import tkinter as tk
from tkinter import ttk , messagebox
import sqlite3


class User : 
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x700")
        self.root.title('User Details')
        self.root.resizable(False,False)

        # ___data
        self.connect=sqlite3.connect('user2.db')
        self.cursor=self.connect.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user2 (
                    id INTEGER,
                    name TEXT,
                    gend TEXT,
                    city TEXT,
                    email TEXT,
                    phone INTEGER PRIMARY KEY
                    )
            ''')
        self.connect.commit()

        # __panedwindow
        self.paned_window=tk.PanedWindow(self.root,orient=tk.VERTICAL)
        self.paned_window.pack(fill=tk.BOTH,expand=True)

        # __top frame
        self.top_frame=tk.Frame(self.paned_window,bg="#f0ead2",width=1200,height=300)
        self.top_frame.pack_propagate(False)
        self.paned_window.add(self.top_frame)

        # ___text
        tk.Label(self.top_frame,text="Name",font=('Bauhaus 93',24),bg="#f0ead2").grid(row=1,column=1,padx=10,pady=10)
        tk.Label(self.top_frame,text="Gend",font=('Bauhaus 93',24),bg="#f0ead2").grid(row=2,column=1,padx=10,pady=10)
        tk.Label(self.top_frame,text="City",font=('Bauhaus 93',24),bg="#f0ead2").grid(row=3,column=1,padx=10,pady=10)
        tk.Label(self.top_frame,text="Email",font=('Bauhaus 93',24),bg="#f0ead2").grid(row=4,column=1,padx=10,pady=10)
        tk.Label(self.top_frame,text="Phone",font=('Bauhaus 93',24),bg="#f0ead2").grid(row=5,column=1,padx=10,pady=10)
        

        # __entry

        # self.margin_left=tk.Label(self.top_frame,text="").grid(row=0,column=1,padx=300)
        self.entry_name=tk.Entry(self.top_frame,font=('Comic Sans MS',15))
        self.entry_gend=tk.Entry(self.top_frame,font=('Comic Sans MS',15))
        self.entry_city=tk.Entry(self.top_frame,font=('Comic Sans MS',15))
        self.entry_email=tk.Entry(self.top_frame,font=('Comic Sans MS',15))
        self.entry_phone=tk.Entry(self.top_frame,font=('Comic Sans MS',15))

        self.entry_name.grid(row=1,column=2,padx=10,pady=10)
        self.entry_gend.grid(row=2,column=2,padx=10,pady=10)
        self.entry_city.grid(row=3,column=2,padx=10,pady=10)
        self.entry_email.grid(row=4,column=2,padx=10,pady=10)
        self.entry_phone.grid(row=5,column=2,padx=10,pady=10)


        # __ butons
        self.button_insert=tk.Button(self.top_frame,text="INSERT",bg="#4fa55e",command=self.insert,padx=20,pady=10,font=('Bauhaus 93',12)).place(x=430,y=100)
        tk.Button(self.top_frame,text="DELETE", bg="red",command=self.delete_row,padx=20,pady=10,font=('Bauhaus 93',12)).place(x=430,y=160)


        # _____n frame
        self.buttom_frame=tk.Frame(self.paned_window,bg='#adc178',width=1200,height=370)
        self.buttom_frame.pack_propagate(False)
        self.paned_window.add(self.buttom_frame,minsize=370)

        # table
        self.columns=('ID',"NAME",'GEND','CITY','EMAIL','PHONE')

        self.style = ttk.Style()
        self.style.configure("Treeview", background="#dde5b6", foreground="black", rowheight=50, fieldbackground="#adc178",font=('Arial', 13))
        self.style.configure("Treeview.Heading", background="#a98467", foreground="#adc178", font=('Arial', 16, 'bold'),)
        self.style.map('Treeview', background=[('selected', '#d7263d')])


        self.tree=ttk.Treeview(self.buttom_frame,columns=self.columns,show="headings",style="Treeview")


        for col in self.columns:
            self.tree.heading(col,text=col)
        
        self.tree.pack(fill=tk.BOTH,expand=True)


        self.update_table()

    def insert(self):
        name=self.entry_name.get()
        gend=self.entry_gend.get()
        city=self.entry_city.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()

        if name=="" or gend=="" or city=="" or email=="" or phone=="":
            messagebox.showerror('error','All feilds must be filled out')
            return
        
        self.cursor.execute('INSERT INTO user2 (id,name,gend,city,email,phone) VALUES (?,?,?,?,?,?)',(id(phone),name,gend,city,email,phone))
        self.connect.commit()
        self.update_table()



    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute('SELECT * FROM user2')
        rows=self.cursor.fetchall()

        for row in rows : 
            self.tree.insert("",'end',values=row)



    def delete_row(self):
        selected_item=self.tree.selection()

        if not selected_item : 
            messagebox.showwarning('No selection','Please select a row to delete.')
            return
        
        confirm=messagebox.askyesno('Confirm Delete','Are you sur eyou want to delete')
        if confirm : 
            for item in selected_item : 
                
                row_values=self.tree.item(item,'values')

                if row_values : 
                    id_value=row_values[0]
                    self.cursor.execute('DELETE FROM user2 WHERE id = ?',(id_value,))
                    self.connect.commit()
                    self.tree.delete(item)

            
            messagebox.showinfo("Success",'Selected row(s) deleted successfully.')

        self.update_table()



if __name__ == "__main__":

    root=tk.Tk()
    window=User(root)
    root.mainloop()