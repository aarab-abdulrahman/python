# Vous êtes responsable d'un système de gestion des données sur les crypto-monnaies. Ces
# données incluent les informations essentielles pour chaque crypto-monnaie, telles que son
# nom, son symbole, son prix actuel, sa capitalisation boursière, et son volume de transactions.
# Objectif : Créer un programme Python pour manipuler une liste de dictionnaires représentant
# différentes crypto-monnaies. Vous devez ajouter, modifier, supprimer, rechercher, filtrer et
# effectuer diverses manipulations sur ces données.
# Structure d’un dictionnaire crypto-monnaie :
# {
#  "name": "Bitcoin", # Nom de la crypto-monnaie
#  "symbol": "BTC", # Symbole de la crypto-monnaie
#  "price": 67000.00, # Prix actuel en USD
#  "market_cap": 1200000000, # Capitalisation boursière en USD
#  "volume": 300000000 # Volume de transactions sur 24h en USD
# }
# Terminologie :
# 1. Créez une liste de dictionnaires contenant des informations fictives sur plusieurs
# crypto-monnaies.
# 2. Ajouter une crypto-monnaie : Une fonction permettant d'ajouter une nouvelle
# crypto-monnaie à la liste.
# 3. Modifier une crypto-monnaie : Une fonction pour mettre à jour les informations
# d'une crypto-monnaie existante.
# 4. Supprimer une crypto-monnaie : Une fonction pour supprimer une crypto-monnaie
# par son symbole.
# 5. Rechercher une crypto-monnaie : Une fonction pour trouver une crypto-monnaie par
# son nom ou son symbole.
# 6. Filtrer les crypto-monnaies : Une fonction pour lister les crypto-monnaies ayant un
# prix ou une capitalisation supérieure/inférieure à une valeur donnée.
# 7. Trier les crypto-monnaies : Une fonction pour trier la liste par prix, capitalisation ou
# volume (ascendant ou descendant).
# 8. Top N crypto-monnaies : Une fonction pour afficher les N premières cryptomonnaies en fonction de la capitalisation.
# 9. Calculer la moyenne des prix ou des capitalisations de toutes les crypto-monnaies.
# 10. Trouver la crypto-monnaie avec la capitalisation ou le volume le plus élevé.



from rich.console import Console
from rich.tree import Tree
import time ,sys


list_crypto=[]

# verification name
def verification_name(x):
    global list_crypto
    if any(x==f['name'] for f in list_crypto):
        return 0
    else :
        return 1

# verification symbole
def verification_symbole(x):
    global list_crypto
    if all(d.isalnum() for d in x) and not any(x == g['symbole'] for g in list_crypto):
        return 'verified'
    else : 
        if any(x == g['symbole'] for g in list_crypto):
            return 'yes'
        else: 
            return 'no'


# verification digits
def verification_digits(x):  #exemple 124.54,65.4
         if x.count('.')<=1 and all(g.isdigit() or g=="." for g in x):
             return 1
         else: 
        
             return 0
         


def input_crypto(list_):
    name=input("type crypto name : ").strip().capitalize()
    if verification_name(name) and name:

        symbole=input("type symbol crypto : ").strip().upper()
        if verification_symbole(symbole)=='verified' and symbole:

            price=input('type the price : ').strip()
            if verification_digits(price) and price:

                market_cap=input("type market cap : ").strip()
                if verification_digits(market_cap) and market_cap:

                    volume=input("type volume : ").strip()
                    if verification_digits(volume) and volume:
                        list_.append({
                            'name':name,
                            'symbole':symbole,
                            'price':float(price),
                            'market cap':float(market_cap),
                            'volume':float(volume)
                        })
                         
                        Console().print('[bold][green]Saved Successfully ![/green][/bold]')
                    else:
                        print("write a number")
                else: 
                    print("write a number")
            else:
                print("write a number")
        else:
            if symbole=="":
             print("write something..")
            elif verification_symbole(symbole)=='yes':
             Console().print("this symbole [red]{}[/red] already exists !".format(symbole))
            elif verification_symbole(symbole)=='no':
              Console().print("this symbole [red]{}[/red] is contient symbols exemple ('-','#','~')".format(symbole))
    
    elif name=="":
        print("write something..")
    else: 
        print("the name already exists !")    


# skipped design
def skipped_design():
    line=Tree('')
    tree_line=line.add('[purple]Skipped[purple]')
    Console().print(line)

# edit list 
def edit_list(x):
    change=0
    global list_crypto
    Console().print("[yellow]type 'enter' or '0' to skip [/yellow]\n")


    name=input("name ---> ").strip().capitalize()
    if name=="0" or name=="":
        skipped_design()
    elif verification_name(name)  :
        list_crypto[x]['name']=name
        change+=1
    else: 
        print("the name already exists !") 
    


    symbole=input("symbol ---> ").strip().upper()
    if symbole=="0" or symbole=="":
        skipped_design()
    elif verification_symbole(symbole)  :  
        list_crypto[x]['symbole']=symbole
        change+=1
    else:
        Console().print("this input -> [red]{}[/red] is contient symbols exemple ('-','#','~')".format(symbole))


    price=input('price ---> ').strip()
    if price=="0" or price=="":
        skipped_design()
    elif verification_digits(price) :
        list_crypto[x]['price']=price
        change+=1
    else:
        print("enter a correct number")


    market_cap=input("type market cap : ").strip()
    if market_cap=="0" or market_cap=="":
        skipped_design()
    elif verification_digits(market_cap) :
        list_crypto[x]['market cap']=market_cap
        change+=1
    else: 
        print("enter a correct number")
    

    volume=input("type volume : ").strip()
    if volume=="0" or volume=="":
        skipped_design()
    elif verification_digits(volume) :
        list_crypto[x]['volume']=volume
        change+=1
    else:
        print("enter a correct number")

    if change>=1:
     if change==1:
      Console().print('[green]One change was successfully registered ✅[/green]')
     else:
      Console().print(f'[green]{change} change were successfully registered ✅[/green]')
    else:
      Console().print("[bold][red]There are no change[/red][/bold] !")
    


# show list
def show_list(list_cry):
        tree=Tree("\n[yellow]List Crypto[/yellow]")
        for index,obj in enumerate(list_crypto,start=1):
          tree_index=tree.add(f"[underline]Crypto no.{index}[/underline]")
          info = (f"| [blue]Name[/blue] : {obj['name']}"
                 f"\n| [blue]symbole[/blue] : {obj['symbole']}"
                 f"\n| [blue]Price[/blue] : {obj['price']}"
                 f"\n| [blue]Market Cap[/blue] : {obj['market cap']}"
                 f"\n| [blue]Volume[/blue] : {obj['volume']}")
          
          tree_index.add(info)
         
        Console().print(tree)


# delete crypto
def delete_crypto(x):
    global list_crypto
    del list_crypto[x]
    Console().print("[green]The list has been deleted .[/green]")

# edit and delete
def del_dit(chose__,my_function):
     if chose__.isdigit() and int(chose__) in [x for x in range(1,len(list_crypto)+1)]:
        my_function(int(chose__)-1)

     else:
         if chose__.isdigit():
           Console().print(f"[red]this number {chose__} is out of range ! [/red]")
         else:
           Console().print("[red]please enter a number ![/red]")

# searching for crypto
def searching_for_crypto(list__,name_or_symbole,inp):
    global download_time
    check=list(filter(lambda l : l[name_or_symbole].lower()==inp.lower(),list__))
    download_time()
    if check : 
      if name_or_symbole=="name":
        Console().print("[black on green] list found ![/black on green]")
        tree=Tree(f"name : {check[0]['name']}")
        tree.add(f"symbole : {check[0]['symbole']}")
        tree.add(f"price : {check[0]['price']}")
        tree.add(f"market cap : {check[0]['market cap']}")
        tree.add(f"volume : {check[0]['volume']}")

        Console().print(tree)
      
      else:
        Console().print("[black on green]list found ![/black on green]")
        tree=Tree(f"symbole : {check[0]['symbole']}")
        tree.add(f"name : {check[0]['name']}")
        tree.add(f"price : {check[0]['price']}")
        tree.add(f"market cap : {check[0]['market cap']}")
        tree.add(f"volume : {check[0]['volume']}")

        Console().print(tree)
      
    else:
        Console().print(f"[bold red]There is no list contiining this {name_or_symbole} : [bold red] [black on red]{inp}[/black on red]")


#download
def download_time():
    items=['-','/','|','\\']
    duration=6
    start=time.time()
    i=0

    while True:
        elapsed_time=time.time()-start
        if elapsed_time >duration:
            break
        sys.stdout.write(f"\rplease white ({items[i]})")
        sys.stdout.flush()
        time.sleep(0.7)

        i+=1
        if i >= 4:
            i=0
    
    sys.stdout.write("\r                         \n")

def show_hide(x):
    if x==0:
     Console().print("""
[cyan]
show / hide ---> menu
1---> add crypto (monnaie)
2---> show list of cryptos
3---> edit crypto
4---> delete crypto
5---> searching for crypto(monnaie)
[/cyan]""") 
     
    else:
        pass

sh=0
while True:
 show_hide(sh)

 y=input("---> ")
 if y=="1":
  input_crypto(list_crypto)

 elif y=="2" and list_crypto:
    show_list(list_crypto)

 elif y=="3" and list_crypto:
     chose=input("enter the number of crypto you want to edit : ").strip()
     del_dit(chose,edit_list)
 
 elif y=="4" and list_crypto:
     chose_2=input("type the number of the item you want yo delete : ").strip()
     del_dit(chose_2,delete_crypto)
 
 elif y=="5" and list_crypto:
     two_options=input('search by (name--> 1 or symbole--> 2) : ').strip()
     if two_options=="1":
         nm=input("write the name : ").strip()
         searching_for_crypto(list_crypto,'name',nm)
     elif two_options=="2":
         sm=input('write the symbole : ').strip()
         searching_for_crypto(list_crypto,'symbole',sm)
     else:
         Console().print("[red]please chose [bold en purple]'1'[/bold en purple] or [bold en purple]'2'[/bold en purple] [/red]")
  
 elif y.lower()=="show":
     sh=0
 
 elif y.lower()=="hide":
     sh=1
     
 elif y in ['1','2','3','4','5'] and not list_crypto :
     Console().print("[bold][black]list is empty ![/black][/bold]")
 else:
     Console().print("[bold][black]select a number from the list[/black][/bold]")