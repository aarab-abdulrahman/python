import tkinter 
from tkinter import messagebox
from rich.console import Console


def  double_N():
    user_input=text_1.get()
    output_area.delete('1.0',tkinter.END)

    if user_input.replace('.','').isdigit() and user_input.count('.')<=1:
        user_input=float(user_input)*2
        output_area.insert(tkinter.END,user_input)
    else:
        Console().messagebox.showwarning('error',f'please type a correct number not [red]{user_input}[/red]')        
    


root=tkinter.Tk()
root.geometry('600x300')
root.title("math")


label_1=tkinter.Label(
    root,
    text="Enter N",
    bg="#fffb05"
)

label_1.grid(row=0,column=0,padx=70)
text_1=tkinter.Entry(
    root,
    relief="solid",
    fg="#333"
)
text_1.grid(row=0,column=1,padx=0,pady=50)



   
label_2=tkinter.Label(
    root,
    text="le double de N : ",
    bg="#fffb05"
)
label_2.grid(row=3,column=0)

output_area=tkinter.Text(
    root,
    height=2,width=40,
)
output_area.grid(row=3,column=1,pady=30)


output=tkinter.Button(
    root,
    text="show output",
    bg="#05ff26",
    command=double_N
)
output.grid(row=2,column=1)


root.mainloop()