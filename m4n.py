import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.box import ROUNDED
from rich.table import Table
import os, time, random, string

def fetch_and_parse_data(query_value):
    url = "https://dbcenter.uk/search"
    data = {
        "q": query_value
    }
    response = requests.post(url, data=data)
    html_data = response.text
    soup = BeautifulSoup(html_data, 'html.parser')
    records = []
    containers = soup.select(".container.card")
    for container in containers:
        record = {}
        record["Full Name"] = container.find("div", string="Full Name").find_next_sibling().text
        record["Phone #"] = container.find("div", string="PHONE #").find_next_sibling().text
        record["CNIC #"] = container.find("div", string="CNIC #").find_next_sibling().text
        record["Address"] = container.find("div", string="Address").find_next_sibling().text
        records.append(record)
    return records
console = Console()
def m4n_header():
    header = """
┳┳┓┏┓┳┓┏┓       
┃┃┃┃┃┃┃┃ ┏┓┓┏┏┓╋
┛ ┗┗╋┛┗┗┛┛ ┗┫┣┛┗
            ┛┛  
    """
    console.print("[bold cyan]" + header + "[/bold cyan]")
    console.print("\n[bold magenta]Where data hides, I seek! - M4N[/bold magenta]\n")
def display_results(results):
    current_index = 0
    while True:
        table = Table(show_header=False, box=ROUNDED)
        result = results[current_index]
        for key, value in result.items():
            table.add_row("[bold blue]{}[/bold blue]".format(key), "[bold green]{}[/bold green]".format(value))
        console.print(table)
        if current_index == 0 and current_index == len(results) - 1:
            console.print("\n[bold magenta]This is the only record.[/bold magenta]")
            break
        elif current_index == 0:
            choice = console.input("\n[bold cyan]Next Record (N) or Exit (E)?[/bold cyan] ").lower()
            if choice == 'n':
                current_index += 1
            else:
                break
        elif current_index == len(results) - 1:
            console.print("\n[bold magenta]This is the last record.[/bold magenta]")
            choice = console.input("[bold cyan]Previous Record (P) or Exit (E)?[/bold cyan] ").lower()
            if choice == 'p':
                current_index -= 1
            else:
                break
        else:
            choice = console.input("\n[bold cyan]Next Record (N), Previous Record (P), or Exit (E)?[/bold cyan] ").lower()
            if choice == 'n':
                current_index += 1
            elif choice == 'p':
                current_index -= 1
            else:
                break
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def hx_e():
    messages = ["Logging IN...", "SUCCESSFULL...!!", "Accessing Database...!!", "Fetching Records...!!"]
    for msg in messages:
        console.print("[bold red]" + msg + "[/bold red]")
        time.sleep(2)
    clear_terminal()
def hx_decrypt():
    for _ in range(5):  
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
        console.print("[bold red]" + random_text + "[/bold red]", end='\r')
        time.sleep(0.2)
    clear_terminal()
    console.print("[bold green]Decryption successful![/bold green]")
    time.sleep(1)
    clear_terminal()
m4n_header()
query_value = input("Enter Phone Number : ")
clear_terminal()
hx_e()
hx_decrypt()
results = fetch_and_parse_data(query_value)
display_results(results)

