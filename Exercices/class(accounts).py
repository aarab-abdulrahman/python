from rich.console import Console
from rich.tree import Tree
console=Console()

class account:
    def __init__(self,name,email,language):
        self.name=name
        self.email=email
        self.language=language
    
    # def __str__(self):
    #     return f" |__full name : {self.name}\n |_email : {self.email} \n |_prefrred language : {self.language}"


accounts=[]
while True : 
    x=input("""
1--> add account
2--> show list account
3--> Exit
---> """)
 

    if x=="1":
        a=input("type your full name : ").strip()
        b=input("type your email : ").strip()
        c=input("type your preferred language : ").strip()
        accounts.append(account(a,b,c))
    elif x=="2":
        tree=Tree("[yellow]Accounts[/yellow]")
        for index , obj in enumerate(accounts,start=1):
            account_tree=tree.add(f"[underline]Account [red]{index}[/red] :[/underline]")
            account_tree.add(f"[green]full name[/green] : {obj.name}")
            account_tree.add(f"[green]email[/green] : {obj.email}")
            account_tree.add(f"[green]preferred language[/green] : {obj.language}")
        console.print(tree)

    elif x=="3":
        break