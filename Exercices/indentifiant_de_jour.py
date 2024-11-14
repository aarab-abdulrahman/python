#Identifiant de Jour
# Demandez à l'utilisateur de saisir une date sous le format "AAAA-MM-JJ". Utilisez des
# conditions pour vérifier si le jour est un week-end ou un jour de semaine. Affichez "Jour de
# semaine" ou "Week-end" en fonction de la date.


from datetime import datetime

try:
    date_str=input("Entrez une date au format 'Y'-'M'-'d' : ").strip()
    date=datetime.strptime(date_str,"%Y-%m-%d")
    
    if date.weekday() < 5 : print("Jour de semaine")
    else: print("Week-end")

except ValueError:
    print('format de date invalide')