"""A library for advanced text management"""

from . import printing, inputs, format

class Color():
    def __init__(self, number: int, name: str):
        if number > 29 and number < 40:
            self.number = number
        else:
            raise NameError(f"No color value '{number}'.")
        if name in ('Black', 'Red', 'Green', 'Yellow', 'Blue', 'White', 'Default'):
            self.name = name
        else:
            raise NameError(f"No color is named '{name.title()}'.")
    
    @classmethod
    def Black(cls) -> 'Color': 
        return cls(30, "Black")
    @classmethod
    def Red(cls) -> 'Color': 
        return cls(31, "Red")
    @classmethod
    def Green(cls) -> 'Color':
        return cls(32, "Green")
    @classmethod
    def Yellow(cls) -> 'Color': 
        return cls(33, "Yellow")
    @classmethod
    def Blue(cls) -> 'Color': 
        return cls(34, "Blue")
    @classmethod
    def White(cls) -> 'Color': 
        return cls(37, "White")
    @classmethod
    def Default(cls) -> 'Color': 
        return cls(39, "Default")

    def __repr__(self):
        return f"Color.{self.name} (number: {self.number}, name: {self.name})"