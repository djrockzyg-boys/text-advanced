"""printing module of **text-advanced**, used for *printing* and *streaming*"""

from __future__ import annotations
import re
import time, typing

if typing.TYPE_CHECKING:
    from . import Color, Style

class Stream():
    def __init__(self, *vals: str):
        self.vals = vals

    def print_stream(self, timer: float = 0.2, sep: str = " ", end: str = '\n') -> None:
        valscomb = sep.join(self.vals)
        vals_split = list(valscomb)
        for val_split in vals_split:
            print(val_split, end="", flush=True)
            time.sleep(timer)
        print(end, end="")

    def print_spaces(self, timer: float = 0.4, sep: str = " ", end: str = '\n'):
        valscomb = sep.join(self.vals)
        vals_split = valscomb.split(" ")
        for val_split in vals_split:
            print(val_split, end=" ", flush=True)
            time.sleep(timer)
        print(end, end="")

    def print_newlines(self, timer: float = 0.3, sep: str = " ", end: str = '\n'):
        valscomb = sep.join(self.vals)
        vals_split = valscomb.split("\n")
        for val_split in vals_split:
            print(val_split, flush=True)
            time.sleep(timer)
    
    def __repr__(self) -> str:
        return f"Stream(vals=\"{' '.join(self.vals)}\")"

def prints(*vals: str, color: Color | None = None, style: Style | None = None, sep: str = " ", end: str = "\n", flush: bool = False):
    """Prints the text as a special color:
    `prints("Hello", color=Color.Red())` Outputs Hello in Red
    """
    if color is None:
        from . import Color
        color = Color.Default()
    if style is None:
        from . import Style
        style = Style.Reset()
    valscomb = sep.join(vals)
    try:
        stylemap = {
            0: "\x1b[0m",
            1: "\x1b[1m",
            2: "\x1b[3m",
            3: "\x1b[1;3m"
        } 
        print(f"\x1b[{color.number}m{stylemap[style.flag]}"+valscomb+"\x1b[0m", end=end, flush=flush)
    except AttributeError as a:
        if a.name == "flag":
            raise ValueError(f'expected \'Style\' but got \'{type(style).__name__}\'.') from None
        else:
            raise ValueError(f'expected \'Color\' but got \'{type(color).__name__}\'.') from None

class BorderText:
    def __init__(self, text: str, color: Color | None = None):
        if color is None:
            from . import Color
            color = Color.Default()
        textsbynw = text.split("\n")
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        texlenmax = max(len(ansi_escape.sub('', s)) for s in textsbynw)
        retlist = []
        retlist.append(f"\x1b[{color.number}m+"+"-" * texlenmax+"+\x1b[0m")
        for textbynw in textsbynw:
            retlist.append(f"\x1b[{color.number}m|\x1b[0m"+textbynw+" " * (texlenmax - len(ansi_escape.sub('', textbynw)))+f"\x1b[{color.number}m|\x1b[0m")
        retlist.append(f"\x1b[{color.number}m+"+"-" * texlenmax+"+\x1b[0m")
        self.retlist = retlist
        self.text = text
    def __repr__(self) -> str:
        return "\n".join(self.retlist)
    def normal(self) -> str:
        return self.text