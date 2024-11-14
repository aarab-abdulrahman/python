#Simulation de Bonus de Performance
# Demandez à l'utilisateur son ancienneté (en années) et sa performance annuelle (entre 1 et 5).
# Utilisez un système de bonus où :
# • Si l’ancienneté est supérieure à 5 ans, et la performance >= 4, le bonus est de 20 % du
# salaire.
# • Si l’ancienneté est inférieure ou égale à 5 ans et la performance >= 4, le bonus est de
# 10 % du salaire.
# • Dans les autres cas, aucun bonus. Affichez le bonus correspondant.

try:
    anciennete = int(input('entre votre anciennete en annees : ').strip())
    performance=int(input('entrez votre performance (entre 1 et 15 ) : ').strip())

    if anciennete > 5 and performance >=4 : print('le bonus est de 20%,du salair')
    elif anciennete<=5 and performance>=4 : print('le bonus est de 10%, de salaire')
    else:print("aucun bonus")

except: print("error")