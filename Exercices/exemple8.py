stock=[]
ask1=input("enter your tasks for today separated by a 'comma or espace': ")
stock+=ask1.replace(' ',',').split(',')
for asking in stock:
 print(f"\n{asking}:")
 ask2=input(f"__did you finish {asking} alredy(yes or no)?: ").capitalize()
 if ask2=="Yes":
  print("nice job")
 elif ask2=="No":
  print("try not to put it off")
 else:
  print("error,write 'yes'or'no'!!")

 print("_ _ _ _ _ _ _ _ _")
input("\nDo you want to get out of the app'type enter': ")
