# Exercice 5 : Ecrire un algorithme qui range trois nombres donné x, y, z, dans
# l'ordre croissant (x < y < z).

def check_id_digit(x):
  if not x.replace('-','').isdigit(): return False
  else :    return True

map=False
digits=[]
while True:
    a=input("entre the number 'x' : ").strip()
    if not check_id_digit(a) : break
    else:
       digits.append(int(a))
       y=input("entre the number 'y' : ").strip()
       if not check_id_digit(y) : break
       else:
          digits.append(int(y))
          z=input("entre the number 'z' : ").strip()
          if not check_id_digit(z) : break
          digits.append(int(z))
    map=True
    break

if map:
    min=digits[0]
    max=digits[0]
    center=None

    for i in digits:
       if i < min : min=i
       elif i> max : max=i
    
    for i in digits:
       if i not in [min,max]: 
          center=i
    
    print(min,' < ',center,' < ',max)

else: print("error")
    
          
