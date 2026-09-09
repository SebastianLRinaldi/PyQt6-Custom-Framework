from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

# from src.helpers import *
from .blueprint import Blueprint

# class Logic(Blueprint):

#     def __init__(self, component):
#         self._map_widgets(component)

#     def update_widget(self) -> None:
#         self.label1.setText("Im on 1, I have been updated by 1!")

#     def reset_widget(self) -> None:
#         self.label1.setText("Im on 1, I have been reset by 1!")


from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from typing import Optional, Union, List, Dict

class Logic:
    """Main logic class for testing various edge cases."""

    # Attributes with and without type hints
    time: int
    status
    label: QLabel
    input_field
    optional_attr: Optional[int]
    union_attr: Union[str, int]
    list_attr: List[str]
    dict_attr: Dict[str, int]

    def __init__(self):
        # Typed attributes
        self.time: int = 0
        self.label: QLabel = QLabel()

        # Untyped attributes
        self.status = "idle"
        self.input_field = None

        # Optional / union types
        self.optional_attr: Optional[int] = None
        self.union_attr: Union[str, int] = 0

        # Complex types
        self.list_attr: List[str] = []
        self.dict_attr: Dict[str, int] = {}

        # Default values edge case
        self.default_number = 42
        self.default_string = "default"

        # Attributes with expressions
        self.computed_value = self.time + 10

    # Methods with docstrings
    def start(self):
        """Start the timer."""
        pass

    def stop(self):
        """Stops the timer completely."""
        pass

    def reset(self):
        pass  # no docstring

    def set_value(self, value: int):
        """Sets the internal value to the given integer."""
        pass

    def load_url(self, url: str):
        """Loads a URL and caches it for later use."""
        pass

    def compute(self, a, b: int):
        """Performs computation."""
        pass

    def void_method(self):
        pass  # no parameters, no docstring

    def mixed_method(self, x, y: str = "default"):
        """Mixed parameters with default value."""
        pass

    def returns_value(self) -> int:
        """Returns a computed integer."""
        return 42

    def returns_none(self) -> None:
        """Explicitly returns None."""
        return None

    def no_return_annotation(self, data):
        """Method without return annotation."""
        pass

    # More complex type annotations
    def optional_param(self, x: Optional[str] = None):
        """Parameter with Optional type."""
        pass

    def union_param(self, value: Union[int, float]):
        """Parameter can be int or float."""
        pass

    def list_param(self, items: List[str]):
        """Parameter is a list of strings."""
        pass

    def dict_param(self, mapping: Dict[str, int]):
        """Parameter is a dictionary of string->int."""
        pass


        
        