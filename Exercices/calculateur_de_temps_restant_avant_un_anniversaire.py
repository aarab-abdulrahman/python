# Calculateur de Temps Restant Avant un Anniversaire
# Demandez à l'utilisateur d'entrer sa date de naissance (jour et mois seulement), puis calculez
# combien de jours il reste jusqu'à son prochain anniversaire à partir de la date actuelle. Utilisez
# des if-else pour gérer le cas où l'anniversaire tombe aujourd'hui et pour calculer l'année
# suivante si l'anniversaire est déjà passé pour cette année.

from datetime import datetime
try : 
    anniversaire_str=input("entrez votre dzte de naissance  ('j'/'MM') : ").strip()
    jour,mois=map(int(),anniversaire_str.split('/'))
    aujourd_hui=datetime.now()

    anniversaire=datetime(aujourd_hui.year,mois,jour)

    if anniversaire < aujourd_hui : 
        anniversaire=datetime(aujourd_hui.year+1,mois,jour)
    jours_restants=(anniversaire-aujourd_hui).days
    if jours_restants==0:
        print("aujourd'hui est votre anniversaire !")
    else:
        print(f"il reste {jours_restants} jours jusqu'a votre anniversaire ")
except ValueError : print("format de date invalide")