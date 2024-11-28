from rich.console import Console
from rich.tree import Tree


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
    if all(d.isalnum() for d in x):
        return 1
    else : return 0

# verification digits
def verification_digits(x):  #exemple 124.54,65.4
         if x.count('.')<=1 and all(g.isdigit() or g=="." for g in x):
             return 1
         else: 
             return 0
         


def input_crypto(list_):
    name=input("type crypto name : ").strip().capitalize()
    if verification_name(name):

        symbole=input("type symbol crypto : ").strip().upper()
        if verification_symbole(symbole):

            price=input('type the price : ').strip()
            if verification_digits(price):

                market_cap=input("type market cap : ").strip()
                if verification_digits(market_cap):

                    volume=input("type volume : ").strip()
                    if verification_digits(volume):
                        list_.append({
                            'name':name,
                            'symbole':symbole,
                            'price':float(price),
                            'market cap':float(market_cap),
                            'volume':float(volume)
                        })
                         
                        Console().print('[bold][green]Saved Successfully ![/green][/bold]')
                    else:
                        print("enter a correct number")
                else: 
                    print("enter a correct number")
            else:
                print("enter a correct number")
        else:
            Console().print("this symbole [red]{}[/red] is contient symbols exemple ('-','#','~')".format(symbole))
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


while True:
 Console().print("""
[cyan]1---> add crypto (monnaie)
2---> show list of cryptos
3---> edit crypto
4---> delete crypto[/cyan]
""") 
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

 elif not list_crypto:
     Console().print("[bold][black]list is empty ![/black][/bold]")