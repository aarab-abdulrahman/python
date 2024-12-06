# Objectif : Comprendre la création de classes, d'objets et l'utilisation des attributs et méthodes.
# • Créez une classe Voiture avec les attributs suivants :
# o marque (string)
# o modele (string)
# o annee (int)
# o kilometrage (int, initialisé à 0)
# • Ajoutez les méthodes suivantes :
# o demarrer : Affiche "La voiture démarre".
# o rouler : Accepte un nombre de kilomètres en paramètre et met à jour kilometrage.
# • Créez un objet de la classe Voiture avec des valeurs pour marque et modele. Appelez ses
# méthodes.
# . Modifiez le constructeur (__init__) pour incrémenter nombre_voitures à chaque création
# d'un objet.
# Ajoutez à la classe Voiture :
# o La méthode __str__ pour afficher les informations sur la voiture (ex. : "Voiture :
# Marque X, Modèle Y")

from rich.console import Console
class Voiture:
    nbr_voiture=0
    def __init__ (self,marque,modele,annee,km):
        self.marque=marque
        self.modele=modele
        self.annee=annee
        self.km=km

        Voiture.nbr_voiture+=1

    def __str__ (self):
        return (f"marque : {self.marque}\n"
                 f"modele : {self.modele}\n"
                 f"annee : {self.annee}\n"
                 f"kilometrage : {self.km}\n")
try: 
    while True:       
        mq=input('\nenter marque name : ').strip()
        modele=input('enter modele name : ')
        annee=int(input('enter annee : '))
        kilometrage=float(input("enter kilometrage : "))
        voi=Voiture(mq,modele,annee,kilometrage)
        print(voi)
        print("nombre des voitures : ",Voiture.nbr_voiture)

except:
    print('error')
               