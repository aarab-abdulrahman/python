import tkinter as tk
from PIL import Image , ImageTk


def diviseur_N():
    n=input_string.get()
    if n.isdigit():
        n=int(n)
        diviseurs=[str(i) for i in range(1,n+1) if n%i==0]

        if diviseurs:
            label_2.config(text="Diviseur de N est : "+" , ".join(diviseurs))
        else:
            label_2.config(text="doesn't exist")
    else:
        label_2.config(text="please enter a valid number.")


root=tk.Tk()
root.geometry('500x200')
root.title('diviseur')

# background color
root.configure(bg='#f0fffd')



label_1=tk.Label(
    root,
    text="Entrer la valeur de N : ",
    fg="#1605ff",
    font=('Comic Sans MS',15)
    
)

label_1.grid(row=0,column=2,padx=150,pady=30)

input_string=tk.Entry(
    root,
    bd=2,relief="solid",
    
)

input_string.grid(row=2,column=2,)

label_2=tk.Label(
    root,
    text="Diviseur de N est : ...",
    fg="#1605ff",
    font=('Comic Sans MS',15)
)
label_2.grid(row=3,column=2,pady=10,padx=0)


button=tk.Button(
    root,
    text="start",
    command=diviseur_N
)
button.place(x=330,y=90)

tk.mainloop()