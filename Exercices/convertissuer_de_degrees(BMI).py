# Convertisseur de Degrés (BMI) : 
# Écrivez un programme qui demande à l'utilisateur son poids et sa taille, puis calcule son
# Indice de Masse Corporelle (IMC). Utilisez if-else pour classer l'utilisateur en sous-poids,
# poids normal, surpoids ou obésité, selon les standards internationaux de l'IMC.

try : 
     poids=float(input('entrer votre poids : ').strip())
     taille=float(input('enter votre taille en metre : ').strip())

     IMC=poids/(taille**2)
     print(f"votre IMC est {IMC:.2f}\n")

     if IMC < 18.5:
          print("sous-poids")
     elif 18.5<=IMC <24.9:
          print("poids normal")
     elif 25<=IMC<29.9:
          print("surpoids")
     else: 
          print("obesite")
except: print('error')
