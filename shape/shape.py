"""This module defines the Shape class."""

from abc import ABC , abstractmethod  

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

class Shape(ABC):
    """Represents a shape."""

    def __init__(self, color : str):
        """Initializes a new instance of the Shape class.
        
            Args:
                color (str): The color of the shape.
                
            Raises:
                ValueError: A ValueError is Raised when color is a blank
                string.
        """
    
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank.")

        self._color = color

    @abstractmethod
    def calculate_area(self) -> float:
        """Calculates the shapes area.
        
        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Calculates the shapes perimeter.
        
        Returns:
            float: The perimeter of the shape.
        """
        pass

    def __str__(self) -> str:
        """Returns a "informal" string representation of 
        the Shape object.
        
        Returns:
            str: The "Informal" string representation of
            the Shape object."""

        return (f"The shape color is {self._color}.")
