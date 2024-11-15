# Écrire une fonction qui prend une date de naissance au format YYYYMM-DD en entrée et renvoie l'âge actuel de la personne.

from datetime import datetime 

try : 
    date_srt=input("type your birth date au format 'Y/M/D' :").strip()
    date=datetime.strptime(date_srt,'%Y/%m/%d')

    now=datetime.now()

    if date<now :
        age=(now -date).days
        age=age//365
        print(f"you age is : {age}")
    else:
        print("your under age")
except :
    print("error")