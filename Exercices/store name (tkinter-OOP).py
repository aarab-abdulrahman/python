import tkinter as tk
import sqlite3
from tkinter import messagebox ,ttk



class Home_Store:

    def __init__(self,root):

        # _____Main
        self.root=root
        self.root.title('Store')
        self.root.geometry("1300x650")
        self.root.resizable(False,False)

        # ____Data
        self.connect=sqlite3.connect('store.db')
        self.cursor=self.connect.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS store (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity INTEGER
                            )
        ''')

        self.connect.commit()

        # ____Panedwindow
        self.paned_window=tk.PanedWindow(self.root,orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH,expand=True)

        # ____first div
        self.left_frame=tk.Frame(self.paned_window,width=700,height=650,bg="#e7ecef")
        self.left_frame.pack_propagate(False)
        self.paned_window.add(self.left_frame)

            # ---> input

        tk.Label(self.left_frame,text="ID",font=('Comic Sans MS',15),bg="#e7ecef").grid(row=1,column=1,padx=10,pady=10)
        tk.Label(self.left_frame,text="Name",font=('Comic Sans MS',15),bg="#e7ecef").grid(row=2,column=1,padx=10,pady=10)
        tk.Label(self.left_frame,text="Price",font=('Comic Sans MS',15),bg="#e7ecef").grid(row=3,column=1,padx=10,pady=10)
        tk.Label(self.left_frame,text="Quantity",font=('Comic Sans MS',15),bg="#e7ecef").grid(row=4,column=1,padx=10,pady=10)

            #----> output

        self.margin_top=tk.Label(self.left_frame,text="",bg="#e7ecef")
        self.entry_id=tk.Entry(self.left_frame,width=20,font=('Comic Sans MS',20))
        self.entry_name=tk.Entry(self.left_frame,width=20,font=('Comic Sans MS',20))
        self.entry_price=tk.Entry(self.left_frame,width=20,font=('Comic Sans MS',20))
        self.entry_quantity=tk.Entry(self.left_frame,width=20,font=('Comic Sans MS',20))

        self.margin_top.grid(row=0,column=2,pady=60)
        self.entry_id.grid(row=1,column=2,padx=10,pady=10)
        self.entry_name.grid(row=2,column=2,padx=10,pady=10)
        self.entry_price.grid(row=3,column=2,padx=10,pady=10)
        self.entry_quantity.grid(row=4,column=2,padx=10,pady=10)


            #---> Buttons
        self.button_1=tk.Button(self.left_frame,text="ENTRY",bg="green",command=self.add_item,highlightbackground="green",highlightthickness=2,font=('Comic Sans MS',15))
        tk.Button(self.left_frame,text="UPDATE",bg="#dede09",command=self.update_item,font=('Comic Sans MS',15)).place(x=220,y=407)
        tk.Button(self.left_frame,text="DELETE",bg="#cb2802",command=self.delete_item,font=('Comic Sans MS',15)).place(x=350,y=407)


        self.button_1.grid(row=5,column=1,padx=10,pady=10)
            #___Bind
        self.button_1.bind('<Enter>',self.on_hover)
        self.button_1.bind('<Leave>',self.on_leave)

        # ___second div
        self.right_frame=tk.Frame(self.paned_window,width=500,height=650,bg='#674e44')
        self.right_frame.propagate(True)
        self.paned_window.add(self.right_frame,minsize=700)


        self.columns=('ID','Name','Price','Quantity')
        # self.tree=ttk.Treeview(self.right_frame,columns=self.columns,show='headings')

        style = ttk.Style()
        style.configure("Treeview", background="#1f7a8c", foreground="black", rowheight=30, fieldbackground="#bfdbf7")
        style.configure("Treeview.Heading", background="#022b3a", foreground="white", font=('Arial', 12, 'bold'),)
        style.map('Treeview', background=[('selected', '#0484d4')])

        self.tree = ttk.Treeview(self.right_frame, columns=self.columns, show='headings', style="Treeview")


        for col in self.columns:
            self.tree.heading(col,text=col)

        self.tree.pack(fill=tk.BOTH,expand=True)

        self.update_table()

    # ____add item (entry)____
    def add_item(self):
        id=self.entry_id.get()
        name=self.entry_name.get()
        price=self.entry_price.get()
        quantity=self.entry_quantity.get()

        if id =="" or name=="" or price=="" or quantity=='':
            messagebox.showerror('error','All fields must be filled out')
            return

        self.cursor.execute("INSERT INTO store (id,name,price,quantity) VALUES (?,?,?,?)",(id,name,price,quantity))
        self.connect.commit()
        self.update_table()
        self.clear_entries()

    def update_item(self):
        id=self.entry_id.get()
        name=self.entry_name.get()
        price=self.entry_price.get()
        quantity=self.entry_quantity.get()

        if id =="" or name=="" or price=="" or quantity=='':
            messagebox.showerror('error','All fields must be filled out')
            return

        self.cursor.execute("UPDATE store SET name = ?,price = ?,quantity = ? WHERE id = ?",(name,price,quantity,id))
        self.connect.commit()
        self.update_table()
        self.clear_entries()

    def delete_item(self):
        id=self.entry_id.get()

        if not id :
            messagebox.showerror('error','ID must be provided to delete item')
            return

        self.cursor.execute("DELETE FROM store  WHERE id = ?",(id,))
        self.connect.commit()
        self.update_table()
        self.clear_entries()

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.cursor.execute("SELECT * FROM store")
        rows=self.cursor.fetchall()

        self.emty_text="No data available"
        if not rows:
            if not hasattr(self,"empty_label"):
                self.empty_label=tk.Label(self.right_frame,text="",bg="#d7263d",font=('Comic Sans MS',20))
                self.empty_label.pack(expand=True,fill=tk.BOTH)
                self.write_text(0)

        else:
            if hasattr(self,'empty_label'):
                self.empty_label.destroy()

        for row in rows:
            self.tree.insert("",'end',values=row)

    def clear_entries(self):
        self.entry_id.delete(0,tk.END)
        self.entry_name.delete(0,tk.END)
        self.entry_price.delete(0,tk.END)
        self.entry_quantity.delete(0,tk.END)

    def close_connection(self):
        self.connect.close()
        self.root.destroy()

    def on_hover(self,event):
        event.widget.config(highlightbackground="black",highlightthickness=2)
    def on_leave(self,event):
        event.widget.config(highlightbackground="green",highlightthickness=2)
        pass
    
    def write_text(self,index):
        if index <len(self.emty_text):
            current_text=self.emty_text[:index+1]
            self.empty_label.config(text=current_text)
            self.root.after(160,self.write_text,index+1)




root=tk.Tk()
wind=Home_Store(root)

root.protocol("WM_DELETE_WINDOW",wind.close_connection)
root.mainloop()

# button=tk.Button(text="hello",highlightbackground="",highlightthickness=)



