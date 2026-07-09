"""printing module of **text-advanced**, used for *printing* and *streaming*"""

from __future__ import annotations
import time, typing

if typing.TYPE_CHECKING:
    from . import Color

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

def prints(*vals: str, color: Color | None = None, sep: str = " ", end: str = "\n", flush: bool = False):
    """Prints the text as a special color
    ```python
    from text_advanced.printing import prints
    from text_advanced import Color
    
    prints("Hello", color=Color.Red()) # Outputs Hello in Red
    ```
    """
    if color is None:
        from . import Color
        color = Color.Default()
    valscomb = sep.join(vals)
    try:
        print(f"\x1b[{color.number}m"+valscomb+"\x1b[0m", end=end, flush=flush)
    except AttributeError:
        raise ValueError(f"type should be 'Color' or 'None' but it is '{type(color).__name__}'.") from None