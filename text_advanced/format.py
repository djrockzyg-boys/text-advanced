from __future__ import annotations
import time, typing

if typing.TYPE_CHECKING:
    from . import Color

class FormatStr(typing.TypedDict):
    color: Color | None
    value: str

def format_terminal(dicts: list[FormatStr]):
    alltexts = []
    for ditc in dicts:
        alltexts.append(f"\x1b[{ditc.color.number}m{ditc.value}\x1b[0m")
    return " ".join(alltexts)