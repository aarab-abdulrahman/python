import subprocess
from rich.console import Console

def check_git_installed():
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_repo_is_in(repo_url):
    try:
        result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True, check=True)
        remotes = result.stdout

        if repo_url in remotes:
            return True
        return False
    except subprocess.CalledProcessError:
        return False


def remove_remote(name):
    subprocess.run(['git','remote','remove',name])

def add_remote_repo(repo_url):
    try:
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        return True
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e):
            Console().print("[yellow]The remote 'origin' already exists.[/yellow]")
        else:
            Console().print("[red]An error occurred while adding the remote.[/red]")
        return False

def affichage_fichiers():
    try:
        result = subprocess.run(['ls'], capture_output=True, text=True, check=True)
        Console().print("[green]Files in the current directory:[/green]")
        print(result.stdout)
    except subprocess.CalledProcessError:
        Console().print("[red]An error occurred while listing files.[/red]")


def get_remotes():
    try:
        result=subprocess.run(['git','remote'],
        capture_output=True,
        text=True,
        check=True)

        result=result.stdout.strip().split('\n')
        for i in result:
            remove_remote(str(i))

    except subprocess.CalledProcessError:
        Console().print("[red]An error occurred while fetching remotes.[/red]")


def push_to_github():
    Console().print("=== Welcome to GitHub Push Helper ===")

    if not check_git_installed():
        Console().print("[red]Git is not installed or not in PATH.[/red]")
        return

    repo_url = input("Enter the repository URL: ").strip()

    if check_repo_is_in(repo_url):
        Console().print("[yellow]The repository already exists.[/yellow]")
    else:
        if add_remote_repo(repo_url):
            Console().print("[green]Remote repository added successfully.[/green]")
        else:
            Console().print("[red]Failed to add the remote repository.[/red]")

    affichage_fichiers()

push_to_github()
