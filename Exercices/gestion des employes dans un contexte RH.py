# Tâches relatives à la gestion des données des employés dans un contexte RH :
# 1. Création d’une liste de dictionnaires pour représenter des employés avec des
# informations comme le nom, la date de recrutement, le salaire, etc.
# 2. Fonctions pour des calculs spécifiques comme le salaire moyen, le nombre d'employés
# par département, enrichissement des données avec un calcul de salaire annuel et
# classification.
# 3. Manipulation des données, comme suppression selon des critères et sauvegarde dans
# un fichier CSV.


from datetime import datetime
employes=[]

def verification_nom(x):
    if any(x.upper() == x['nom'].upper() for x in employes):
        return False
    else : 
        return True

def verifiation_salaire(x):
    if x.replace('.','').isdigit() and float(x)>0 :
        return True
    else :
        return False

def verification_date(x):
    try:
        x=datetime.strptime(x,'%Y-%m-%d')
        return True
    except:
        return False
    
def entree(employes):
    nom=input("ecrivez votre nom : ").strip()
    if verification_nom(nom):
        date_recrutement=input("entrez la date de recrutement sous forme ('Y'-'M-'d') : ").strip()
        if verification_date(date_recrutement):
            salaire=input("entrer le salaire : ").strip()
            if verifiation_salaire(salaire):
                departement=input("entrez le departement par exemple ('It' ou 'RH' or 'Marketing' or ...) : ").strip()
                employes.append({
                    'nom':nom,
                    'date de recrutement':date_recrutement,
                    'salaire':float(salaire),
                    'departement':departement
                })
            else :print("error")
        else: print("error!")
    else:
        print("error!")


entree(employes)
x=input("type enter to show menu")
print(employes)