import tkinter as tk 
from tkinter import ttk , messagebox


contries=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 
'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 
'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 
'China', 'Colombia', 'Comoros', 'Congo (Congo-Brazzaville)', 'Congo (Congo-Kinshasa)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 
'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 
'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 
'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 
'Kazakhstan', 'Kenya', 'Kiribati', 'Korea (North)', 'Korea (South)', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 
'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 
'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 
'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 
'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 
'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 
'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 
'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 
'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']


def insert_item():

    name=entry_name.get()
    last_name=entry_last_name.get()
    contry=entry_contry.get()
    phone=entry_phone_number.get()
    children=entry_children.get()

    try: 
        gender_=int(gender.get())


        if name=="" or last_name=="" or contry=="" or phone=="" or children=="" or gender=="" :
            messagebox.showerror('error','Please make sure to fill all the info')
            return

        for child in tree.get_children():
            phone_exists=tree.item(child,'values')[3]
            if phone == phone_exists:
                messagebox.showerror('error','phone number already exists!')
                return
            
        if gender_:
            gender_="male"
        else:
            gender_="female"
        
        tree.insert("","end",values=(name,last_name,contry,phone,children,gender_))
    
    except:
        messagebox.showerror('error','Please make sure to fill all the info')

        
def delete_item():
    selection_item=tree.selection()

    if not selection_item : 
        messagebox.showwarning('no selection','please select item to delete')
    
    ask_to_delete=messagebox.askyesno('Confirme delete','are you sur you want to delete.')

    if ask_to_delete: 
        
        for item in selection_item : 
            tree.delete(item)
        
        messagebox.showinfo('success','Selected row(s) deleted successfully')

# ______________________
root=tk.Tk()
root.geometry("1200x500")
root.title('Contacts')

right_frame=tk.Frame(root)
left_frame=tk.Frame(root)
raduis_button_frame=tk.Frame(root)

right_frame.pack(side="right",fill="y")
left_frame.pack(side='left',fill="y")
# __________________________

# lebel
name=tk.Label(left_frame,text="name",font=13).grid(row=1,column=1,padx=10,pady=10)
last_name=tk.Label(left_frame,text="last name",font=13).grid(row=2,column=1,padx=10,pady=10)
contry=tk.Label(left_frame,text="Contry",font=13).grid(row=3,column=1,padx=10,pady=10)
phone_number=tk.Label(left_frame,text="phone number",font=13).grid(row=4,column=1,padx=10,pady=10)
gender=tk.Label(left_frame,text="gender",font=13).grid(row=5,column=1,padx=10,pady=10)
Number_of_your_children=tk.Label(left_frame,text="Number of your children",font=13).grid(row=6,column=1,padx=10,pady=10)


gender=tk.StringVar()

# entry
entry_name=tk.Entry(left_frame,font=20,fg="green")
entry_last_name=tk.Entry(left_frame,font=20,fg="green")
entry_contry=ttk.Combobox(left_frame,values=contries,font=20,state="readonly")
entry_phone_number=tk.Entry(left_frame,font=20,fg="green")

tk.Radiobutton(raduis_button_frame,text="Male",variable=gender,value=1,fg="green").pack(side="left")
tk.Radiobutton(raduis_button_frame,text="Female",variable=gender,value=0,fg="green").pack(side="left")

entry_children=tk.Spinbox(left_frame,font=20,fg="green",from_=0,to=10,state='readonly')


entry_name.grid(row=1,column=2,padx=10,pady=10)
entry_last_name.grid(row=2,column=2,padx=10,pady=10)
entry_contry.grid(row=3,column=2,padx=10,pady=10,sticky="news")
entry_phone_number.grid(row=4,column=2,padx=10,pady=10)
raduis_button_frame.place(x=250,y=190)
entry_children.grid(row=6,column=2,padx=10,pady=10)

# buttons
insert_button=tk.Button(left_frame,text="INSERT",font=20,command=insert_item,bg="green",activebackground="#00ff15",activeforeground="white")
delete_button=tk.Button(left_frame,text="DELETE",font=20,command=delete_item,bg="#f22929",activebackground='red',activeforeground="white")

insert_button.grid(row=7,column=1,pady=20)
delete_button.grid(row=7,column=2,pady=20)

# tree
column=('name','last name','contry','phone number','gender','children')

tree=ttk.Treeview(right_frame,columns=column,show="headings")

for col in column:
    tree.heading(col,text=col)
    tree.column(f'{col}',width=120)

tree.pack(fill='both',side='right')

root.mainloop()
