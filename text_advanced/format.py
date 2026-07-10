from __future__ import annotations
import typing, re

if typing.TYPE_CHECKING:
    from . import Color, Style

class FormatStr(typing.TypedDict):
    color: Color | None = None
    style: Style | None = None
    value: str

class TerminalDictFormat:
    def __init__(self, dicts: list[FormatStr]):
        for ditc in dicts:
            if not 'color' in ditc:
                from . import Color
                ditc['color'] = Color.Default()
            if not 'style' in ditc:
                from . import Style
                ditc['style'] = Style.Reset()
        self.dicts = dicts

    def print_values(self):
        print(" ".join([ditc["value"] for ditc in self.dicts]))
    
    def print_formatted(self):
        stylemap = {
                0: "",
                1: "\x1b[1m",
                2: "\x1b[3m",
                3: "\x1b[1;3m"
        }
        alltexts = []
        for ditc in self.dicts:
            alltexts.append(f"{stylemap[ditc['style'].flag]}\x1b[{ditc['color'].number}m{ditc['value']}\x1b[0m")
        print(*alltexts)
    
    def get_values(self):
        return " ".join([ditc["value"] for ditc in self.dicts])

    def get_formatted(self):
        stylemap = {
                0: "",
                1: "\x1b[1m",
                2: "\x1b[3m",
                3: "\x1b[1;3m"
        }
        alltexts = []
        for ditc in self.dicts:
            alltexts.append(f"{stylemap[ditc['style'].flag]}\x1b[{ditc['color'].number}m{ditc['value']}\x1b[0m")
        return " ".join(alltexts)

class TerminalStrFormat:
    def __init__(self, string: str):
        self.string = string
    
    def print_formatted(self):
        for1 = re.sub(r"\[bold\](.*?)\[/bold\]", "\x1b[1m\\1\x1b[0m", self.string)
        for2 = re.sub(r"\[italic\](.*?)\[/italic\]", "\x1b[3m\\1\x1b[0m", for1)
        for3 = re.sub(r"\[red\](.*?)\[/red\]", "\x1b[31m\\1\x1b[0m", for2)
        for4 = re.sub(r"\[green\](.*?)\[/green\]", "\x1b[32m\\1\x1b[0m", for3)
        for5 = re.sub(r"\[yellow\](.*?)\[/yellow\]", "\x1b[33m\\1\x1b[0m", for4)
        for6 = re.sub(r"\[blue\](.*?)\[/blue\]", "\x1b[34m\\1\x1b[0m", for5)
        for7 = re.sub(r"\[white\](.*?)\[/white\]", "\x1b[37m\\1\x1b[0m", for6)
        for8 = re.sub(r"\[black\](.*?)\[/black\]", "\x1b[30m\\1\x1b[0m", for7)
        for9 = re.sub(r"\[bolditalic\](.*?)\[/bolditalic\]", "\x1b[1;3m\\1\x1b[0m", for8)
        print(for9)
    
    def print_values(self):
        for1 = re.sub(r"\[bold\](.*?)\[/bold\]", r"\1", self.string)
        for2 = re.sub(r"\[italic\](.*?)\[/italic\]", r"\1", for1)
        for3 = re.sub(r"\[red\](.*?)\[/red\]", r"\1", for2)
        for4 = re.sub(r"\[green\](.*?)\[/green\]", r"\1", for3)
        for5 = re.sub(r"\[yellow\](.*?)\[/yellow\]", r"\1", for4)
        for6 = re.sub(r"\[blue\](.*?)\[/blue\]", r"\1", for5)
        for7 = re.sub(r"\[white\](.*?)\[/white\]", r"\1", for6)
        for8 = re.sub(r"\[black\](.*?)\[/black\]", r"\1", for7)
        for9 = re.sub(r"\[bolditalic\](.*?)\[/bolditalic\]", r"\1", for8)
        print(for9)
    
    def get_formatted(self):
        for1 = re.sub(r"\[bold\](.*?)\[/bold\]", "\x1b[1m\\1\x1b[0m", self.string)
        for2 = re.sub(r"\[italic\](.*?)\[/italic\]", "\x1b[3m\\1\x1b[0m", for1)
        for3 = re.sub(r"\[red\](.*?)\[/red\]", "\x1b[31m\\1\x1b[0m", for2)
        for4 = re.sub(r"\[green\](.*?)\[/green\]", "\x1b[32m\\1\x1b[0m", for3)
        for5 = re.sub(r"\[yellow\](.*?)\[/yellow\]", "\x1b[33m\\1\x1b[0m", for4)
        for6 = re.sub(r"\[blue\](.*?)\[/blue\]", "\x1b[34m\\1\x1b[0m", for5)
        for7 = re.sub(r"\[white\](.*?)\[/white\]", "\x1b[37m\\1\x1b[0m", for6)
        for8 = re.sub(r"\[black\](.*?)\[/black\]", "\x1b[30m\\1\x1b[0m", for7)
        for9 = re.sub(r"\[bolditalic\](.*?)\[/bolditalic\]", "\x1b[1;3m\\1\x1b[0m", for8)
        return for9
    
    def get_values(self):
        for1 = re.sub(r"\[bold\](.*?)\[/bold\]", r"\1", self.string)
        for2 = re.sub(r"\[italic\](.*?)\[/italic\]", r"\1", for1)
        for3 = re.sub(r"\[red\](.*?)\[/red\]", r"\1", for2)
        for4 = re.sub(r"\[green\](.*?)\[/green\]", r"\1", for3)
        for5 = re.sub(r"\[yellow\](.*?)\[/yellow\]", r"\1", for4)
        for6 = re.sub(r"\[blue\](.*?)\[/blue\]", r"\1", for5)
        for7 = re.sub(r"\[white\](.*?)\[/white\]", r"\1", for6)
        for8 = re.sub(r"\[black\](.*?)\[/black\]", r"\1", for7)
        for9 = re.sub(r"\[bolditalic\](.*?)\[/bolditalic\]", r"\1", for8)
        return for9