from text_advanced.format import TerminalStrFormat
from text_advanced import Style, Color

main = TerminalStrFormat("[green][bold]Hello Guys[/bold][/green]")
lolbro = main.get_values()
print(lolbro)