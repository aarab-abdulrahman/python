# Demander à l'utilisateur de saisir une date au format YYYY-MM-DD et
# afficher quel jour de la semaine correspond à cette date.

from datetime import datetime

date1=input("type a date 'Y/M/D': ").strip()
date1_obj=datetime.strptime(date1,"%Y/%m/%d")

days=['monday','tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
nbr_day=date1_obj.weekday()
print("le  jour corresoand a cette date est : {}".format(days[nbr_day]))









