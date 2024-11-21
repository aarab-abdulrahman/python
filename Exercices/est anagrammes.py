# Créer une fonction pour vérifier si deux mots sont des anagrammes

def anagrammes(word1 ,word2):
    return sorted(word1)==sorted(word2)

try:
    word1=input("type a word : ").strip().lower()
    word2=input("type a word : ").strip().lower()
    print("est anagramme ? ---> ",anagrammes(word1,word2))
except : print("error")