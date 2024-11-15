# Écrire un programme qui prend la date actuelle et calcule le nombre
# de jours restants jusqu'à la fin de l'année.

from datetime import datetime
try: 
    date_actuelle=input("type the current date Y/m/d :").strip()
    date_actuelle=datetime.strptime(date_actuelle,"%Y/%m/%d")
    year=date_actuelle.year + 1 

    date_fin=datetime.strptime(f"{year}/1/1","%Y/%m/%d")

    difference=(date_fin-date_actuelle).days

    print(f"le nombre de jours restants jusqu'a la fin de lanne est : {difference}")

except: print("error")
