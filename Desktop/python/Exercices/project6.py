stock_emoji=[ "👊", "✋", "✌️" ]
guess_number=[]
stock_imoji2=[]
#radnom
import random
guess=random.randint(0,2)
guess_number.append(guess)
#
ask1=input("welcome to the rock , paper , scissors game:\n_Press enter to continue or type 'Help' for the rules:  ,").capitalize()
if ask1!="Help" and ask1:
 print("please type enter to continue or type 'Help',say again♻️")
else:
 if ask1=="Help":
  print("""
  ****RULES****
  1) You choose and the computer chooses
  2) Rock smashes Scissors -> Rock wins
  3) Scissors cut paper -> Scissors win
  4) Paper covers Rock -> Paper win
  """)
 else:
  print("ok...")
 #ask2
 ask2=input("\nenter your choise (rock or paper or scissors): ").lower()
 #proba
 if ask2=="rock":
  stock_imoji2.append(stock_emoji[0])
  #print
  print(f"you chose:\n{stock_imoji2[0]}")
  print(f"\n\ncomputer chose:\n{stock_emoji[guess]}")
  #proba
  if guess_number[0]==0:
   print("\ndraw")
  if guess_number[0]==1:
    print("\nyou lose")
  elif guess_number[0]==2:
    print("\nyou win")
 elif ask2=="paper":
  stock_imoji2.append(stock_emoji[1])
  #print
  print(f"you chose:\n{stock_imoji2[0]}")
  print(f"\n\ncomputer chose:\n{stock_emoji[guess]}")
  #proba
  if guess_number[0]==1:
   print("\ndraw")
  if guess_number[0]==0:
    print("\nyou win")
  elif guess_number[0]==2:
    print("\nyou lose")
 elif ask2=="scissors":
  stock_imoji2.append(stock_emoji[2])
  #print
  print(f"you chose:\n{stock_imoji2[0]}")
  print(f"\n\ncomputer chose:\n{stock_emoji[guess]}")
  #proba
  if guess_number[0]==2:
   print("\ndraw")
  if guess_number[0]==0:
    print("\nyou lose")
  elif guess_number[0]==1:
    print("\nyou win")

 else:
  print("please write rock or paper or scissors")