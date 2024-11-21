# Créer une fonction qui analyse un texte donné.
# • Question : Écrivez une fonction analyze_text(text) qui prend en paramètre une
# chaîne de caractères text. La fonction doit retourner un dictionnaire contenant :
# • Le nombre total de mots dans le texte.
# • Le nombre total de mots dans le texte qui repete ,
# • Le nombre de mots uniques et des lettres uniques. 
# .use easy methode



def analyze_text(text):
    text = text.lower()
    
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    
    words = text.split()

    total_words = len(words)

    unique_words = set(words)  
    num_unique_words = len(unique_words)

    repeated_words = [word for word in unique_words if words.count(word) > 1]
    num_repeated_words = len(repeated_words)

    letters = ''.join(words) 
    unique_letters = set(letters) 
    num_unique_letters = len(unique_letters)

    return {
        "total_words": total_words,
        "repeated_words": num_repeated_words,
        "unique_words": num_unique_words,
        "unique_letters": num_unique_letters
    }

try:
    text = input("type a sentence : ").strip()
    print(analyze_text(text))

except: print("wrong")
