from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter

global_text=""
restart=False
continue_=False

def reset():
    global global_text ,restart,continue_

    if restart:
        result_final.config(text='',fg="white")
        entry_text.config(text="")
        restart=False
        global_text=""

    if continue_:
        result_final.config(text='')


def on_click(value):
    global global_text ,restart,continue_
    reset()

    wrap=0
    width=12
    if len(global_text)>width:
        wrap+=11
        width+=12

    if value=="=":
        try:
            continue_=True
            result_final.config(text=f"= {str(eval(global_text))}")
        except:
            restart=True
            result_final.config(text="error",fg="red")

    elif value=="AC":
        global_text=""
        entry_text.config(text="")

    elif value in  ["0","1","2","3","4","5","6","7","8","9","+","/","-","%","*"]:
        global_text+=value
        new_text=global_text[wrap:]
        entry_text.config(text=new_text)

    else: 
        print(global_text)
    print(global_text)


window = Tk()

window.geometry("301x520")
window.configure(bg = "#121212")


canvas = Canvas(
    window,
    bg = "#121212",
    height = 520,
    width = 301,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    300.0,
    515.0,
    fill="#121212",
    outline="")

button_image_1 = PhotoImage(
    file="button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('='),
    relief="flat"
)
button_1.place(
    x=221.0,
    y=436.0,
    width=60.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file="button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('-'),
    relief="flat"
)
button_2.place(
    x=221.0,
    y=304.0,
    width=60.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file="button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('*'),
    relief="flat"
)
button_3.place(
    x=221.0,
    y=238.0,
    width=60.0,
    height=60.0
)

button_image_4 = PhotoImage(
    file="button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('/'),
    relief="flat"
)
button_4.place(
    x=221.0,
    y=172.0,
    width=60.0,
    height=60.0
)

button_image_5 = PhotoImage(
    file="button_5.png")
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('%'),
    relief="flat"
)
button_5.place(
    x=155.0,
    y=172.0,
    width=60.0,
    height=60.0
)

button_image_6 = PhotoImage(
    file="button_6.png")
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('+/-'),
    relief="flat"
)
button_6.place(
    x=89.0,
    y=172.0,
    width=60.0,
    height=60.0
)

button_image_7 = PhotoImage(
    file="button_7.png")
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('AC'),
    relief="flat"
)
button_7.place(
    x=23.0,
    y=172.0,
    width=60.0,
    height=60.0
)

button_image_8 = PhotoImage(
    file="button_8.png")
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('9'),
    relief="flat"
)
button_8.place(
    x=155.0,
    y=238.0,
    width=60.0,
    height=60.0
)

button_image_9 = PhotoImage(
    file="button_9.png")
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('8'),
    relief="flat"
)
button_9.place(
    x=89.0,
    y=238.0,
    width=60.0,
    height=60.0
)

button_image_10 = PhotoImage(
    file="button_10.png")
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('7'),
    relief="flat"
)
button_10.place(
    x=23.0,
    y=238.0,
    width=60.0,
    height=60.0
)

button_image_11 = PhotoImage(
    file="button_11.png")
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('6'),
    relief="flat"
)
button_11.place(
    x=155.0,
    y=304.0,
    width=60.0,
    height=60.0
)

button_image_12 = PhotoImage(
    file="button_12.png")
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('5'),
    relief="flat"
)
button_12.place(
    x=89.0,
    y=304.0,
    width=60.0,
    height=60.0
)

button_image_13 = PhotoImage(
    file="button_13.png")
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('4'),
    relief="flat"
)
button_13.place(
    x=23.0,
    y=304.0,
    width=60.0,
    height=60.0
)

button_image_14 = PhotoImage(
    file="button_14.png")
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('3'),
    relief="flat"
)
button_14.place(
    x=155.0,
    y=370.0,
    width=60.0,
    height=60.0
)

button_image_15 = PhotoImage(
    file="button_15.png")
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('2'),
    relief="flat"
)
button_15.place(
    x=89.0,
    y=370.0,
    width=60.0,
    height=60.0
)

button_image_16 = PhotoImage(
    file="button_16.png")
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('1'),
    relief="flat"
)
button_16.place(
    x=23.0,
    y=370.0,
    width=60.0,
    height=60.0
)

button_image_17 = PhotoImage(
    file="button_17.png")
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('0'),
    relief="flat"
)
button_17.place(
    x=20.0,
    y=436.0,
    width=130.0,
    height=60.0
)

button_image_18 = PhotoImage(
    file="button_18.png")
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click(','),
    relief="flat"
)
button_18.place(
    x=155.0,
    y=436.0,
    width=60.0,
    height=60.0
)

button_image_19 = PhotoImage(
    file="button_19.png")
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_click('+'),
    relief="flat"
)
button_19.place(
    x=221.0,
    y=370.0,
    width=60.0,
    height=60.0
)

button_image_20 = PhotoImage(
    file="button_20.png")
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
    x=135.0,
    y=0.0,
    width=35.0,
    height=35.0
)

button_image_21 = PhotoImage(
    file="button_21.png")
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
# button_21.place(
#     x=135.0,
#     y=35.0,
#     width=39.0,
#     height=35.0
# )

button_image_22 = PhotoImage(
    file="button_22.png")
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=20.0,
    y=100.0,
    width=63.0,
    height=49.0
)




# ____________________________
entry_text=tkinter.Label(
    window,
    text="",
    bg="#121212",
    fg="gray",
    font=("Arial",18,"bold")
)
entry_text.place(x=95,y=83)

result_final=tkinter.Label(
    window,
    text="",
    bg="#121212",
    fg="white",
    font=("Arial",28,"bold")
)
result_final.place(x=95,y=110)

window.resizable(False, False)
window.mainloop()
