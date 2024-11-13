# Exercice 5 : Ecrire un algorithme qui range trois nombres donné x, y, z, dans
# l'ordre croissant (x < y < z).

def check_id_digit(x):
  if not x.replace('-','').isdigit(): return False
  else : 
     x=int(x)
     return True

map=False
digits=[]
while True:
    a=input("entre the number 'x' : ").strip()
    if not check_id_digit(a) : break
    else:
       digits.append(a)
       y=input("entre the number 'y' : ").strip()
       if not check_id_digit(y) : break
       else:
          digits.append(y)
          z=input("entre the number 'z' : ").strip()
          if not check_id_digit(z) : break
          digits.append(z)
    map=True
    break

if map:
   max_=max(digits)
   digits.remove(max(digits))
   min_=min(digits)
   digits.remove(min(digits))

   print(min_,' < ',*digits,' < ',max_)

else: print("error")
    
          
