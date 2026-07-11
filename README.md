# Text Advanced
- A library for advanced text management
- see the [docs](https://text-advanced.readthedocs.io/en/)
### Some Examples:
```python
from text_advanced.printing import prints
from text_advanced import Color

prints("Yo guys what's up!", color=Color.Red())

```
```python
from text_advanced import Color

# All colors of text_advanced
Color.Red()
Color.Black()
Color.Green()
Color.Yellow()
Color.Blue()
Color.White()
Color.Default()
```

# CHANGELOG
### Module Added
- `text_advanced.format`
### Classes Added:
- `class FormatStr(TypedDict)`:
```python
[
    {
        'color': Color.Red(),
        'value': 'Yo guys'
    },
    {
        'style': Style.Bold(),
        'value': 'wassup'
    }
]
```
- `TerminalStrFormat(dicts: list[FormatStr])`
  - `print_formatted()`
  - `print_values()`
  - `get_formatted() -> str`
  - `get_values() -> str`
- `TerminalDictFormat()`
  - `print_formatted()`
  - `print_values()`
  - `get_formatted() -> str`
  - `get_values() -> str`
- One Example:
```python
from text_advanced.format import TerminalStrFormat

formt = TerminalStrFormat(
    "[bold]Yo[/bold] [red]wassup![/red]"
)
```
- `BorderText(text: str, color: Color)`
  - `normal()` - Returns normal text
  - `print(BorderText(...))` - Returns text enclosed in a border
