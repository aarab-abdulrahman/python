from rich.console import Console
class Voiture:
    def __init__ (self,marque,modele,annee,km):
        self.marque=marque
        self.modele=modele
        self.annee=annee
        self.km=km
    def __str__ (self):
        return (f"marque : {self.marque}\n"
                 f"modele : {self.modele}\n"
                 f"annee : {self.annee}\n"
                 f"kilometrage : {self.km}\n")
try:        
    mq=input('enter marque name : ').strip()
    modele=input('enter modele name : ')
    annee=int(input('enter annee : '))
    kilometrage=float(input("enter kilometrage : "))
    voi=Voiture(mq,modele,annee,kilometrage)
    print(voi)

except:
    print('error')
               