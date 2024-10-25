stock_number=[]
name=[]
print("***  welcome to ishop calculator ***")
ask1=input("how many items are there in yourr basket today (type number)?: ")
if not ask1.isdigit() :
 print("error,please type number!")
else :
 for x in range(1,int(ask1)+1):
  print("let's get to counting them...")
  ask2=input(f"\nplease tell me the name of the item number {x}: ").capitalize()
  name.append(ask2)
  ask3=input(f"what is the price of {ask2} :$")
  if ask3.replace(".", "", 1).isdigit():
   number=float(ask3)
   stock_number.append(number)
  else:
   print(f"please type number and not: {ask3}")
 ask4=input("would you like to see your entire basket items(yes or no)?: ").lower()
 if ask4=="yes":
  print(name)
 elif ask4=="no":
  print('ok')
 else:
  print("error, please enter yes or no")
 ask5=input("would you like to see how much it'll cost(yes or no)?: ").upper()
 if ask5=="YES":
  print(f"${sum(stock_number)}")
 elif ask5=="NO":
  print("ok")
 else:
  print("please type yes or no")
 ask6=input('type enter to exit...')
