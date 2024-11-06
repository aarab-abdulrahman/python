#decimal en binaire :
def decimale_en_binaire(x):
 binaire=[]
 while x>0:
     binaire.append(str(x%2))
     x=x//2
 binaire.reverse()
 return ''.join(binaire)
 

#binaire en decimal
def binaire_en_decimal(x):
  x=x[::-1]
  x=list(x)
  decimale=0
  if not '1'in x and  not '0' in x:
      return False
  else:
      for i in range(len(x)):
          decimale+=int(x[i])*(2**i)
  return decimale
  
 #--------------------------------------------------- 
    

print("""
 1---> Convert decimal en binary
 2---> Convert binary en decimal
""")
a=input("entre your choice : ").strip()
if a=='1':
   try : 
       x=int(input("entre a number : ").strip())
       print('------>',decimale_en_binaire(x))
   except:
       print("error")
elif a=='2':
    try:
       x=input("entre a number : ").strip()
       print('---->',binaire_en_decimal(x))
    except:
        print("error")
    