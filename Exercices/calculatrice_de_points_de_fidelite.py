# Écrivez un programme qui demande à l'utilisateur combien il a dépensé dans un magasin.
# Calculez des points de fidélité selon des seuils définis (par exemple : moins de 50€ = 0
# points, entre 50€ et 100€ = 1 point tous les 10€, plus de 100€ = 1 point tous les 5€). Utilisez
# des if-else pour ajuster les points selon les dépenses.


def calculter_point(x):
     if x < 50:
          return 0
     elif 50 <= x <=100 : return x//10
     elif x>100 : return x//5

try :
     depenses=float(input("combien avez-vous depense dans de magasin ? : ").strip())
     print(f"vous avez depense {depenses} euro , vous avez gage {calculter_point(depenses)} points de fidelite")

except: print('error')