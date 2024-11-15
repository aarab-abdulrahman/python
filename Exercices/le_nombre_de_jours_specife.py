# Écrire une fonction qui prend une date et un nombre de jours comme
# paramètres et renvoie la date après avoir ajouté le nombre de jours
# spécifié.

from datetime import datetime,timedelta
try : 
    date1=input("type adate in format 'Y-M-D' : ")
    day =int(input("typr how much days do you want to add 'D' :"))

    date1_obj=datetime.strptime(date1,"%Y-%m-%d")

    newdate=(date1_obj + timedelta(days=day))

    print(f"new date : {newdate.strftime('%Y-%m-%d')}")


except : print("error")