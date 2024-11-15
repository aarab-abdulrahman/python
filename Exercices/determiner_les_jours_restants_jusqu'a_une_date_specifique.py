# Déterminer les Jours Restants Jusqu'à une Date Spécifique :
# Demandez à l'utilisateur de saisir une date future au format JJ/MM/AAAA (par exemple, une
# date de rendez-vous ou d'événement). Calculez et affichez le nombre de jours restants jusqu'à
# cette date. Si la date est dans le passé, affichez un message indiquant que la date est déjà
# passée

from datetime import datetime

def jours_restants():
    date_string=input("Entrez une date future 'JJ/MM/AA' : ").strip()
    try: 
        date_obj=datetime.strptime(date_string,'%d/%m/%Y')
        aujourd_hui=datetime.now()
        if date_obj>aujourd_hui : 
            difference=date_obj-aujourd_hui
            print(f"il rest {difference.days} jours")
        else: 
            print("la date est deja passe")
    except ValueError : 
        print("format de date invalide")


jours_restants()
