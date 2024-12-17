from ttkbootstrap import ttk , font ,Button
import ttkbootstrap as tb
from PIL import Image,ImageTk
from tkinter import StringVar
import tkinter 


error=False
def on_click(x):
    global error
    current=label_display['text']
    if x=="=":
        try : 
         label_display.config(text=str(eval(current)),fg='green')
        except:
            label_display.config(text="error",fg='red')
            error = not error
    elif x=="C":
        label_display.config(text='',fg='white')
    elif x=="<-":
        if error:
         current=""
         error = not error
        label_display.config(text=current[:-1],fg='white')
    else:
        if error:
          current=""
          error = not error
        label_display.config(text=current+x,fg="white")



def change_page(name_page):
    for frame in pages.values():
        frame.pack_forget()
    # pages[name_page].grid(row=0, column=0, sticky="nsew") 


# __________________Main application_________________________
root=tb.Window(themename="darkly")
root.geometry("400x500")
root.title('Calculator')
root.resizable(False,False)

icon_image=Image.open("calculator_35118.ico")
icon_photo=ImageTk.PhotoImage(icon_image)

root.iconphoto(False,icon_photo)
# ____________________________________________
 
# navigation bar 
nav_bar=ttk.Frame(root,bootstyle="superhero")
# nav_bar.grid(sticky="ew",row=0,column=0)

pages={}
page1=ttk.Frame(root,bootstyle="darkly")
page2=ttk.Frame(root,bootstyle="superhero")
pages['page1']=page1
pages['page2']=page2

btn_history=ttk.Button(
    nav_bar,
    text='history',
    bootstyle="success-link",
    command=change_page('page2')
)

# btn_history.grid(row=0,column=1)

btn_home=ttk.Button(
    nav_bar,
    text="home",
    bootstyle="danger-link",
    command=change_page('page1')
)
# btn_home.grid(row=0,column=2)

# _____________________________

buttons={
    ('-',2,2), ('/',2,3) , ('*',2,4),
    ('7',3,2), ('8',3,3) , ('9',3,4),
    ('4',4,2), ('5',4,3) , ('6',4,4),
    ('1',5,2), ('2',5,3) , ('3',5,4),
    ('0',6,2),  ('.',6,3) , ('+',6,4),
    ('C',7,2), ('<-',7,3) ,('=',7,4)
}
for txt , rw , col in buttons :
    button=Button(
       root,
        text=txt,
        command= lambda t=txt : on_click(t),
        padding=(45,20),
        bootstyle="danger",
    )
    if txt in ['0','1','2','3','4','5','6','7','8','9']:
        button.config(bootstyle='info')
    elif txt=="=":
        button.config(bootstyle='success')
    elif txt==".":
        button.config(padding=(46,20))
    elif txt=='<-':
        button.config(padding=(41,20))
    elif txt in ["+","=",'C']:
        button.config(padding=(44,20))
      
    button.grid(row=rw,column=col,padx=2,pady=2)



margin_left=ttk.Label(
    root,
    text=""
)
margin_left.grid(row=2,column=0,padx=17)

margin_top=ttk.Label(
    root,
    text=""
)
margin_top.grid(row=0,column=1,pady=30)

# result=StringVar()
label_display=tkinter.Label(
    root,
    width=40,
    # style="success",
    # textvariable=result
    font=("Arial", 20)  

)
label_display.place(y=30,x=-120)




root.mainloop()
