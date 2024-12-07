import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox,filedialog



encryption_map = {
     'a': '@', 'b': '#', 'c': '$', 'd': '%', 'e': '&',
     'f': '*', 'g': '!', 'h': '~', 'i': '^', 'j': '?',
     'k': '+', 'l': '=', 'm': '-', 'n': '_', 'o': '|',
     'p': '<', 'q': '>', 'r': '/', 's': '[', 't': ']',
     'u': '{', 'v': '}', 'w': ':', 'x': ';', 'y': '"',
     'z': "'", ' ': ' '  
}

decryption_map={v:k  for k,v in encryption_map.items()}

def encryption(text):
    encrypted_text=""
    for character in text.lower():
        if character in encryption_map:
          encrypted_text+=encryption_map[character]
        else:
           encrypted_text+=character
    return encrypted_text

def decryption(text):
   decryption_text=""
   for encryption in text.lower() :
      if encryption in decryption_map:
         decryption_text+=decryption_map[encryption]
      else: 
         decryption_text+=encryption
   return decryption_text



def encryption_text():
   text=text_1.get("1.0",tkinter.END)
   result=encryption(text)
   text_2.delete("1.0",tkinter.END)
   text_2.insert("1.0",result)

def decryption_text():
   text=text_1.get("1.0",tkinter.END)
   result=decryption(text)
   text_2.delete("1.0",tkinter.END)
   text_2.insert("1.0",result)

def copy_to_clipboard():
   root.clipboard_clear()
   root.clipboard_append(text_2.get("1.0",tkinter.END))

def copy_to_clipboard2():
   root.clipboard_clear()
   root.clipboard_append(text_1.get("1.0",tkinter.END))

def clear_text():
   text_1.delete("1.0",tkinter.END)
   text_2.delete("1.0",tkinter.END)

def save_file():
  text_1_save=text_1.get("1.0",tkinter.END)
  text_2_save=text_2.get("1.0",tkinter.END)

  if not text_1_save.strip() or not text_2_save.strip():
   messagebox.showwarning("warning","please enter text to save and encrypted it...")
   return
  
  file_path=filedialog.asksaveasfilename(defaultextension="text_save.txt",filetypes=[('text files','*.txt')])
  
  if file_path:
     text_add="\n----------input------------\n\n"+text_1_save+"\n-----------output-----------\n\n"+text_2_save
   
     with open(file_path,'w') as file:
        file.write(text_add)

def save_text_2():
   save_text_2=text_2.get("1.0",tkinter.END)
   if not save_text_2.strip():      
      messagebox.showwarning("warning","please encrypted a text....")
      return  
   file_path_text_2=filedialog.asksaveasfilename(defaultextension="text_save.txt",filetypes=[('text files','*.txt')])
   if file_path_text_2:
      with open(file_path_text_2,'w') as file2:
          file2.write(save_text_2)


#debut
root=tkinter.Tk()
root.title('encryption by abdu')
# root.geometry('800x600')
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

#icon
icon_image=ImageTk.PhotoImage(file="icon.png")
root.iconphoto(True,icon_image)


text_1=tkinter.Text(
   root,
   height=40,width=75,
   font=('Comic Sans MS',15),
   bg='#e6eaef',
   fg='#333',bd=4,
   relief='groove'
 )

text_1.place(x=20,y=85,width=600,height=590)


text_2=tkinter.Text(
   root,
   height=40,width=75,
   bg='#fffacd',
   fg='#333',
   bd=4,
   relief='groove',
   font=('Comic Sans MS', 15))
text_2.place(x=745,y=85,width=600,height=590)


#clear button
clear_image=Image.open("clear.png")
clear_image=clear_image.resize((50,47),Image.LANCZOS)
clear_photo=ImageTk.PhotoImage(clear_image)
clear_button=tkinter.Button(image=clear_photo,command=clear_text,bd=0)
clear_button.place(x=685,y=248)


#encryption button
encrypte_image=Image.open("encrypt.png")
encrypte_image=encrypte_image.resize((120,40),Image.LANCZOS)
encryption_photo=ImageTk.PhotoImage(encrypte_image)
encryption_button=tkinter.Button(image=encryption_photo,command=encryption_text,bd=0)
encryption_button.place(x=620,y=200)


#decryption
decrypt_image = Image.open("decrypt.png")  
decrypt_image = decrypt_image.resize((120, 40), Image.LANCZOS)
decrypt_photo = ImageTk.PhotoImage(decrypt_image)
decrypt_button = tkinter.Button( image=decrypt_photo, command=decryption_text, bd=0)
decrypt_button.place(x=620,y=303)

#save file
save_image = Image.open("saveall.png")  
save_image = save_image.resize((48, 45), Image.LANCZOS)
save_photo = ImageTk.PhotoImage(save_image)
save_button = tkinter.Button( image=save_photo, command=save_file, bd=0)
save_button.place(x=625,y=250)


# copy to colipboard 2
copy_image2 = Image.open("copy.png") 
copy_photo2 = ImageTk.PhotoImage(copy_image2)
copy_button2 = tkinter.Button( image=copy_photo2, command=copy_to_clipboard, bd=0)
copy_button2.place(x=744,y=671)


#copy to colipboard 1
copy_image1=Image.open("copy1.png")
copy_imgae1=copy_image1.resize((200,1),Image.LANCZOS)
copy_photo1=ImageTk.PhotoImage(copy_image1)
copy_button1=tkinter.Button(image=copy_photo1,command=copy_to_clipboard2,bd=0)
copy_button1.place(x=19,y=671)


save_text_2_image=Image.open("save2.png")
save_text_2_image=save_text_2_image.resize((30,60),Image.LANCZOS)
save_text_2_photo=ImageTk.PhotoImage(save_text_2_image)
save_text_2_button=tkinter.Button(image=save_text_2_photo,command=save_text_2,bd=0)
save_text_2_button.place(x=716,y=84)



input_photo=tkinter.PhotoImage(file="input.png")
image_label=tkinter.Label(root,image=input_photo,bd=0)
image_label.place(x=158,y=42)


root.mainloop()