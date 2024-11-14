# Analyse de Numéros de Carte de Crédit : 
# Demandez à l'utilisateur de saisir un numéro de carte de crédit. Vérifiez le format (16
# chiffres) et identifiez le type de carte selon le premier chiffre (4 pour Visa, 5 pour
# Mastercard, etc.). Ensuite, faites une vérification simple du numéro (par exemple, vérifier la
# somme des chiffres, ou un autre critère) et indiquez si le numéro est "valide" ou "non valide"
# selon vos critères.

numero_carte=input("entrer un numero de carte : ").strip

if len(numero_carte)==16 and numero_carte.isdigit():
    if numero_carte[0]=='4': type_carte='visa'
    elif numero_carte[0]=='5': type_carte='mastercard'
    else : type_carte = 'incunnu'

    print("type de carte est {}".format(type_carte))
    
    somme=sum(int(x) for x in numero_carte)
    if somme%10==0: print("le numero de carte est valide")
    else: print("le numero de carte est non valide ")

else: 
    print('le numero de carte doit etre egal a 16')