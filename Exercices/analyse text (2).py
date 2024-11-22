#Une fonction Python analyze_text pour analyser un texte.
def analyse_text(x):
    text_split=x.split()
    
    # nombre des mots
    nbr_mots=len(text_split)

    #nombre des caracters (sans espace)
    sum_caracters=sum(len(word) for word in text_split)

    #nombre des caracters delimitees par '!' et '.' et '?'
    nbr_caracters_delimitees=x.count('!')+x.count('.')+x.count('?')

    return {
        'nombre des mots : ':nbr_mots,
        'somme des caracters :':sum_caracters,
        'nombre des caracters delimitees par (! et . et ?) : ':nbr_caracters_delimitees
    }


a=input('Ecrire une phrase : ').strip()
if a : 
    print(analyse_text(a))
else:
    print("elle n'a rien ecrit...")

