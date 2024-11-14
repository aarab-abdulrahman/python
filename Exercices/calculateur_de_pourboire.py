# Calculateur de Pourboire : 
# Demandez à l'utilisateur le montant total d'une addition et la qualité du service (excellent,
# bon, mauvais). Calculez le pourboire en fonction de la qualité (par exemple : 20 % pour
# excellent, 15 % pour bon, 5 % pour mauvais). Utilisez if-else pour ajuster le pourcentage.



try :
    montant_total=float(input('Entrez le montant total : ').strip())
    while True:
     qualite_service=input("Enrez le quantite du service 'excellent' or 'bon' or 'mauvais' : ").strip().lower()
     if qualite_service=="excellent": 
        porcentage_pourboire=0.25 
        break
     elif qualite_service=="bon":
        porcentage_pourboire=0.15
        break
     elif qualite_service=="mauvais":
        porcentage_pourboire=0.05
        break
     else:
        print("qualite service non reconnue ...\n")
    
    pourboire=montant_total*porcentage_pourboire

    print(f"pourboire : {pourboire:.2f} euro")
    print(f"Totale a payer : {montant_total+pourboire:.2f} euro")

except: print("error")