import string
import random
password=[]
#
ask=input("enter the totale number of characters in the password: ")
ask2=input('enter the number of letters in the password: ')
ask3=input('enter the number of numbers in the password: ')
ask4=input('enter the number of symbols in the password: ')
if int(ask2)+int(ask3)+int(ask4)==int(ask) and (ask and ask2 and ask3 and ask4).isdigit():
 password+=random.choices(string.ascii_letters,k=int(ask2))
 password+=random.choices(string.digits,k=int(ask3))
 password+=random.choices(string.punctuation,k=int(ask4))
 random.shuffle(password)
 print(''.join(password))

else:
 print('The numbers you entered do not correspond to the required number an make sure you write a number!')
