# Vérificateur de Fin de Mois
# Écrire un programme qui demande à l'utilisateur de saisir une date et vérifie si cette
# date tombe en fin de mois (le dernier jour du mois). Utilisez des if-else pour afficher "Fin
# de mois" ou "Non" en fonction du jour.


from datetime import datetime,timedelta

try : 
    date_saisie=input('entrer une date "Y-M-D" : ').strip()
    date_obj=datetime.strptime(date_saisie,'%Y-%m-%d')

    dernier_jour_mois=(date_obj.month != (date_obj + timedelta(days=1)).month)
    if dernier_jour_mois : 
        print("fin de mois")
    
    else:
        print("non")

except: print("error")




