#tarhib
print("""welcome to 'chose wellet'
you will give me a list of (names) ,and I will pick a person to pay
""")
#il asmaa
fir=input("\n if you're ready , enter the names separated by a 'comma' 🔴 :")
if fir :
 print("ok , let's continue⚡...")
 #split
 spl=fir.split(",")
 #3adad il horof
 int_number=int(len(spl) -1)
 #random
 import random
 rand=random.randint(0,int_number)
 #print
 print(f"please ask '{spl[rand]}', to take his wallet out. dinner is on him🐯")
else :
 print("there is a problem , you didn't write anything ❗❗")