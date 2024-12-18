from ttkbootstrap import ttk , font ,Button
import ttkbootstrap as tb
from PIL import Image,ImageTk
# from tkinter import StringVar
import tkinter 


error=False
def on_click(x):
    global error
    current=label_display['text']
    if x=="=":
        try : 
         label_display.config(text=str(eval(current)),fg='#09ff00')
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
    pages[name_page].pack(fill="both",expand=True)


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
nav_bar=ttk.Frame(root,bootstyle="cyborg")
nav_bar.pack(fill="x",side="top")

pages={}
page1=ttk.Frame(root,bootstyle="cyborg")
page2=ttk.Frame(root,bootstyle="cyborg")
pages['page1']=page1
pages['page2']=page2



btn_home=ttk.Button(
    nav_bar,
    text="home",
    bootstyle="danger-link",
    command=lambda : change_page('page1')
)
# btn_home.pack(side='left')

change_page('page1')

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
        page1,
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
    page1,
    text="",
    
)
margin_left.grid(row=2,column=0,padx=17)

margin_top=ttk.Label(
    page1,
    text="",
)
margin_top.grid(row=0,column=1,pady=30)

# result=StringVar()
label_display=tkinter.Label(
    page1,
    width=40,
    # style="success",
    # textvariable=result
    font=("Arial", 20)  ,
    # height=2,
    # bg="#303030",

)
label_display.place(y=30,x=-110)


# _______________page2________________

icon_history=Image.open("history.png")
icon_history=icon_history.resize((40,40))
photo_history=ImageTk.PhotoImage(icon_history)

btn_history=ttk.Button(
    nav_bar,
    image=photo_history,
    bootstyle="success-link",
    command=lambda : change_page('page2')
)

btn_history.pack(side='right')


root.mainloop()
