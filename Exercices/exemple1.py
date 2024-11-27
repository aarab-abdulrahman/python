data=[]
print("hello welocome to my app")
first=input("add the first color you like: ")
print("ok")
second=input("do you want to add more (yes or no ): ").lower()
data.append(first)
if second=="yes":
 print("beautiful")
 finallly=input("add another color to teh list: ")
 data.append(finallly)
 print(f"the color you like are: {data} ")
elif second=="no":
 print("ok")
 print(f"the color you like are: {data}")
else :
 print("please write 'yes' or 'no'")
