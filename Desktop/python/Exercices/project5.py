ilha9l=['🌿', '🌿', '🌿'],['🌿', '🌿', '🌿'],['🌿', '🌿', '🌿']
print("welcome to place the rabbit")
print(f"{ilha9l[0]}\n{ilha9l[1]}\n{ilha9l[2]}")
ask=input("where should the rabbit gp 🐰?\n__please choose a row a column (add comma or / or space): ")
#deep
les_ask=len(ask)
int1=int(ask[0])
int2=int(ask[2])
if les_ask==3 :
 if 1<=int1<=3 and 1<=int2<=3:
  ilha9l[int1-1][int2-1]="🐰"
  print(f"{ilha9l[0]}\n{ilha9l[1]}\n{ilha9l[2]}")
 else:
  print("___please choose two of these numbers (1,2,3)")
else :
 print("Add the 'space or comma or ..' between the two numbers and choose two of these numbers (1 or 2 or 3")