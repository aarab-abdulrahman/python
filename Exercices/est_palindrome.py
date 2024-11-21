# Manipuler les dates et les chaînes de caractères pour vérifier si
# une date est un palindrome.
# • Question : Écrivez une fonction is_date_palindrome(date) qui prend une date au
# format "DD-MM-YYYY" en paramètre et vérifie si la date est un palindrome (c'est-àdire si elle se lit de la même manière à l'envers, sans tenir compte des tirets).
# Retournez True ou False.
# • Indice : Utilisez la méthode .replace() pour supprimer les tirets et .reverse() pour
# vérifier si la date est un palindrome.


def is_date_palindrome(date):
    date_without_hyphens = date.replace("-", "")
    
    return date_without_hyphens == date_without_hyphens[::-1]

try: 
    date1=input("entre date , format('Y'-'M'-'d') ").strip()
    print(" is palindrome ? ----> ",is_date_palindrome(date1)) 
except : print("error")

