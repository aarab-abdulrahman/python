# Validateur de Mot de Passe : 
# Écrire un programme qui demande un mot de passe à l'utilisateur et vérifie s'il respecte les
# règles suivantes :
# • Au moins 8 caractères
# • Contient au moins une lettre majuscule, une lettre minuscule, un chiffre, et un
# caractère spécial (par exemple, !@#$%^&*) Afficher un message indiquant si le mot
# de passe est "valide" ou "non valide", et spécifier les critères manquants le cas
# échéant.


password=input("entre your password : ")

long_min= len(password)>=8
upper_case=any(x.isupper() for x in password)
lower_case=any(x.islower() for x in password)
number=any(x.isdigit() for x in password)
caracters=any(x in '@#$%^&*' for x in password)

if long_min and upper_case and lower_case and number and caracters : 
    print("le mot de passe est valide ")
else:
    print("le mod de passe est non valide")