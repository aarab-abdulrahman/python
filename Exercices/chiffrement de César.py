# Chiffrement de César
# Implémentez un chiffrement de César. Il s'agit d'un simple chiffrement par substitution où
# chaque lettre d'un texte est décalée d'un certain nombre de positions dans l'alphabet.
# Instructions :
# 1. Écrivez une fonction encrypt_caesar(text, shift) qui prend un texte text et un entier
# shift pour décaler chaque lettre.
# 2. Écrivez la fonction inverse decrypt_caesar(cipher_text, shift) pour déchiffrer le texte.
# 3. Gérez les majuscules et minuscules, mais ignorez les caractères non alphabétiques.


def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            new_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            print(new_char)
            if char.isupper():
                new_char = new_char.upper()
            encrypted_text += new_char
        else:
            encrypted_text += char 
    return encrypted_text

def decrypt_caesar(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha(): 
            new_char = chr(((ord(char.lower()) - 97 - shift) % 26) + 97)
            if char.isupper():
                new_char = new_char.upper()
            decrypted_text += new_char
        else:
            decrypted_text += char  
    return decrypted_text

text = "a"
shift = 3

encrypted = encrypt_caesar(text, shift)
decrypted = decrypt_caesar(encrypted, shift)

print("Encrypted Text:", encrypted)  
print("Decrypted Text:", decrypted)  
