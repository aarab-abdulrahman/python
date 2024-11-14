# Analyseur de Texte :
# Demandez à l'utilisateur une phrase et utilisez des conditions pour :
# • Vérifier si la phrase contient au moins une voyelle.
# • Vérifier si la longueur de la phrase est un multiple de 3.
# • Afficher un message en fonction du résultat des deux conditions


try : 
    sentence=input('Veuillez entrer une phrase : ').strip()
    voyelle_condition=any(x in sentence.lower() for x in 'aeiou')
    est_mult_3=len(sentence)%3 == 0

    if voyelle_condition and est_mult_3 : 
        print('la phrase contient au moins une voyelle avec sa longeur est un multiple de 3.')
    elif voyelle_condition : 
        print('la phrase contient au moins une voyelle .')
    elif est_mult_3:
        print("la longeur de la phrase est un multiple de 3.")
    else:
        print("la phrase ne contient pas de voyelles et sa longeur n'est pas multiple de 3.")


except: print("error")