stock=[]
print("welcome to..")
ask1=input('enter the names of attendees separated by commas or espace!!: ')
stock += ask1.replace(" ", ",").split(',')
print(stock)
for attendance in stock:
 print(f"\n{attendance}")
 ask2=input("is this person attending (yes or no)?: ").upper()
 if ask2=="YES":
  print(f"{attendance},attendance confirmed")
 elif ask2=="NO":
  print(f"{attendance},attendance not confirmed")
 else:
  print("error!,please write yes or no")
 print("_ _ _ _ _ _ ")
