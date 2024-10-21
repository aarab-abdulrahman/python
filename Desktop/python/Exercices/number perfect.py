#number perfect 
def number_perfect(x):
    if x<=0:
        return 0
    
    somme_diviseur = sum ([i for i in range(1,x) if x%i==0])

    if somme_diviseur == x:return 1
    else: return 0

try :
 a=input("type a number : ").replace(' ','')
 a=int(a)
 if number_perfect(a):
    print("{} is number perfect".format(a))
 else:
    print("{} is not number perfect".format(a))
except:
   print("type a number please...")