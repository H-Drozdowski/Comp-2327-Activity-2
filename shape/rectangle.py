"""This module defines the Rectangle class."""

from shape.shape import Shape

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

class Rectangle(Shape):

    def __init__(self, color : str, length : int, width : int):
        """Initializes a new instance of the Rectangle class.
        
        Args:
            length (int): Represents the length of two opposing sides of
            the Rectangle in centimeters.
            width (int): Represents the width of two opposing sides of 
            the Rectangle in centimeters.
            
        """

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")

        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")
        
        super().__init__(color)