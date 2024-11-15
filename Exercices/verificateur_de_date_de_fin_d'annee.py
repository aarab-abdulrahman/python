# Vérificateur de Date de Fin d'Année
# Écrire un programme qui demande une date et vérifie si elle tombe le dernier jour de l'année
# (c’est-à-dire, le 31 décembre). Affichez "Fin d'année" ou "Non" en fonction de la date saisie.

from datetime import datetime
def fin_annee() : 
   date_str=input("enter une date : ").strip()
   date_obj=datetime.strptime(date_str,"%d/%m/%Y")
   if date_obj.month==12 and date_obj.day ==31 :
      print("fin d'annee")
   else:
      print("non")

fin_annee()
