# Devine mon Nombre : 
# Créez un programme où l'ordinateur choisit un nombre entre 1 et 100. Demandez à
# l’utilisateur de deviner ce nombre. Si la réponse est trop basse ou trop haute, donnez-lui un
# indice pour l’aider. Utilisez des conditions if-else pour gérer chaque réponse de l'utilisateur et
# limiter le nombre de tentatives à 5.

from random import randint

rand=randint(1,101)
print(rand)
try:
    for i in range(5):
     n=int(input("entre a number between (1-100) : ").strip())
     if n==rand :
        print("Correct")
        break
     elif rand-5<n<rand: print("you are close to the answer . the number is small")
     elif rand<n<rand+5 : print("you are close to the answer . the number is large")
     else:print('False')


except: print("please entre a number")