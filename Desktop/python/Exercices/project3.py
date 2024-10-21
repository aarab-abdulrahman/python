#data
database1=[]
database2=[]
print("""
welcome to,
(*):means necessary and unbearable
""")
ask1=input("enter the name of a book you own(*): ").lower()
database1.append(ask1)
if ask1 :
 print("good, let's continue")
 #so3al ba3din
 print("")
 ask2=input("enter the name of another book you own(or press'enter' to skip) : ").lower()
 print("")
 if ask2 :
  database1.append(ask2)
 else :
  print("ok")
 print(f"your library : {database1}")
 #ask3
 ask3=input("enter the name of abook you wish to have in the future(*): ").lower()
 print("")
 if ask3:
  print("ok...")
  database2.append(ask3)
  #ask4
  ask4=input("enter the name of another book you wish to have (or press 'enter' to skip): ").lower()
  if ask4 :
   database2.append(ask4)
  else :
   print("ok")
  print("")
  #________________
  print(f"your wishlist: {database2}")
  #ask5
  ask5=input("enter the name of a book from your wishlist that you're acquired (or prees 'enter' to skip): ").lower()
  print("")
  if ask5 in database2 :
   print("ok,...")
   database2.remove(ask5)
   database1.append(ask5)
  else:
   print("ok,...")
  #jam3data
  print(f"updated library : {database1}")
  print(f"updated wishlist: {database2}")
  #ask6
  ask6=input("enter the name of a book from your library you wish yo donate (or press 'enter' to skip): ").lower()
  print("")
  if ask6 in database1 and ask6:
   database1.remove(ask6)
   print(f"final library after donations : {database1}")
  elif ask6 not in database1 and ask6:
   print(f"'{ask6}' ,There's a line in the kidney!!.")
  else :
   print(f"__final library after donations is : {database1}")
 else :
  print("erorr,you didn't write anything!!")
else :
 print("erorr,you didn't write anything!!")