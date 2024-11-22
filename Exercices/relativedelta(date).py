# développer une fonction dateAdd(startDate, critere) retourne une date en fonction du critére  , le critére peut être nombre années , nombre mois , nombre jour ....
# développer une fonction dateSub(startDate,critere)
# développer une fonction qui prend n seconds et retourne le nombre d heures , minute et seconde

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def dateAdd(startDate, critere):

    date_obj = datetime.strptime(startDate, "%Y-%m-%d")
    jours = critere.get('jours', 0)
    mois = critere.get('mois', 0)
    annees = critere.get('annees', 0)
    
    date_obj += timedelta(days=jours)
    date_obj += relativedelta(months=mois, years=annees)
    
    return date_obj.strftime("%Y-%m-%d")

def datesub(startDate, critere):
    date_obj=datetime.strptime(startDate,'%Y-%m-%d')
    jours=critere.get('jours',0)
    mois=critere.get('mois',0)
    annees=critere.get('annees',0)
    date_obj -= timedelta(days=jours)

    date_obj -= relativedelta(months=mois,years=annees)
    return date_obj.strftime("%Y-%m-%d")

def convertseconds(x):
    heures=x//3600
    minutes=(x%3600)//60
    seconds=(x%60)
    return 'heures : ',heures,'\nminutes : ',minutes,'\nseconds : ',seconds 

# try: 
a=input("type a date ('Y-M-d') : ").strip()
b=input("date add : ").strip()
annnees,mois,jours=map(int,b.split(','))
if len(b.split(',')) != 3:
    raise ValueError("Please provide exactly 3 values for years, months, and days.")
print('date add ---> ',dateAdd(a,{"annees":annnees,"mois":mois,"jours":jours}))
print('date sub ---> ',datesub(a,{"annees":annnees,"mois":mois,"jours":jours}) )

n=int(input('enter number of secondes : ').strip())
print(convertseconds(n))

# except ValueError as a : print(f'error !,please enter a number and date not {a}')

