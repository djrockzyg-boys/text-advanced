# text-advanced
## Points:
- A python library made for text management.
- Uses no other dependencies.

## Class:
### `Color(number: int, name: str)`:
- A color class for terminal color
#### All colors are:
```python
Color.Red()
Color.Black()
Color.Green()
Color.Yellow()
Color.Blue()
Color.White()
Color.Default()
```

## Modules:
### inputs:
#### `selector(prompt, selected_prompt)`:
- this is used for input in a rich style, Ex:
```python
from text_advanced.inputs import selector

ask = selector("What is the date?")
```

- Output will be:
```
What is the date? >>
```
- After entering some date like **8-7-2026**, the text would change to:
```
Selected Option (8-7-2024)
```

### printing:
#### class `Stream(*values)`:
- this class is used for streaming outputs
```python
from text_advanced.printing import Stream

textstr = Stream("Hello What's up")
```
##### `print_stream(timer: float, sep: str, end: str)`:
- prints the text letter by letter

##### `print_spaces(timer: float, sep: str, end: str)`:
- prints the text space by space
##### `print_newline(timer: float, sep: str, end: str)`:
- prints the text newline by newline

#### function `prints(*vals: str, color: Color | None, sep, end: str, flush: bool)`:
- prints the string with a **specific color**.

# CHANGE LOG
- latest release
