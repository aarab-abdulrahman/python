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
                         
                        Console().print('[green]succesfully ![/green]')
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
    Console().print("[yellow]type 'enter' to skip or '0'[/yellow]\n")


    name=input("name ---> ").strip().capitalize()
    if name=="0" or name=="":
        skipped_design()
    elif verification_name(name)  :
        list_crypto[x-1]['name']=name
        change+=1
    else: 
        print("the name already exists !") 
    


    symbole=input("symbol ---> ").strip().upper()
    if symbole=="0" or symbole=="":
        skipped_design()
    elif verification_symbole(symbole)  :  
        list_crypto[x-1]['symbole']=symbole
        change+=1
    else:
        Console().print("this input -> [red]{}[/red] is contient symbols exemple ('-','#','~')".format(symbole))


    price=input('price ---> ').strip()
    if price=="0" or price=="":
        skipped_design()
    elif verification_digits(price) :
        list_crypto[x-1]['price']=price
        change+=1
    else:
        print("enter a correct number")


    market_cap=input("type market cap : ").strip()
    if market_cap=="0" or market_cap=="":
        skipped_design()
    elif verification_digits(market_cap) :
        list_crypto[x-1]['market cap']=market_cap
        change+=1
    else: 
        print("enter a correct number")
    

    volume=input("type volume : ").strip()
    if volume=="0" or volume=="":
        print("skipeed")
    elif verification_digits(volume) :
        list_crypto[x-1]['volume']=volume
        change+=1
    else:
        print("enter a correct number")

    if change>=1:
     Console().print('[green]succesfully ![/green]')
    else:
      Console().print("[red]no change[/red]")
    


while True:
 y=input("""
1---> add crypto (monnaie)
2---> show list of cryptos
3---> edit crypto
---> """) 
 if y=="1":
  input_crypto(list_crypto)
 elif y=="2":
     tree=Tree("\n[yellow]List Crypto[/yellow]")
     for index,obj in enumerate(list_crypto,start=1):
         tree_sort=tree.add(f"[underline]Crypto no.{index}[/underline]")
         info = (f"| [blue]Name[/blue] : {obj['name']}"
                 f"\n| [blue]symbole[/blue] : {obj['symbole']}"
                 f"\n| [blue]Price[/blue] : {obj['price']}"
                 f"\n| [blue]Market Cap[/blue] : {obj['market cap']}"
                 f"\n| [blue]Volume[/blue] : {obj['volume']}")
         
         tree_sort.add(info)

     Console().print(tree)
 elif y=="3":
     chose=input("enter the number crypto of liste you want to edit : ").strip()
     if chose.isdigit() and int(chose) in [x for x in range(1,len(list_crypto)+1)]:
        edit_list(int(chose)-1)

     else:
         if chose.isdigit():
           Console().print(f"[red]this number {chose} is out of range ! [/red]")
         else:
            Console().print("[red]please enter a number ![/red]")