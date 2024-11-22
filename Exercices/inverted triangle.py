def inverted_triangle(x):
    for i in range(x,0,-1):
        line=''.join(str(c) for c in range(1,i+1))
        print(line)

try:
    n=int(input("Entrez le nombre de lignes pour le triangle inverse : ").strip())
    inverted_triangle(n)

except ValueError: 
    print("error! , please type a number ")