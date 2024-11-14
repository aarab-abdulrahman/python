#Convertisseur de Temps:
# Créez un programme qui convertit un format de temps de 24 heures (HH) en format 12
# heures (exemple : "14:30" devient "2:30 PM"). Utilisez if-else pour gérer les cas AM/PM.


def convert_to_pm(x):
    hours,minutes=map(int,x.split(':'))

    if hours==0 : return f"12:{minutes:02d} AM"
    elif hours==12 : return f"12:{minutes:02d} PM"
    elif hours>12: return f"{hours-12}:{minutes:02d} PM"
    else: return f"{hours}:{minutes:02d} AM"

try: 
    time=input("entre time 'hours:minutes' : ").strip()
    print(convert_to_pm(time))

except: print("error")