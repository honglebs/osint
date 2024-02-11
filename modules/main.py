from rich import print

from rich.console import Console
from rich.theme import Theme
console = Console(theme=Theme({"repr.number": "bold green blink"}))
console.print("The total is 128")

print("Hello, [bold green]Geeks[/bold green]!")
print("[italic red]Hello[/italic red] World!")

def main():
    return
