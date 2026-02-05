"""This module defines the Rectangle class."""

from shape import Shape

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

class Rectangle(Shape):
    """Represents a Rectangle."""

    def __init__(self, color : str, length : int, width : int):
        """Initializes a new instance of the Rectangle class.
        
        Args:
            length (int): Represents the length of two opposing sides of
                the Rectangle in centimeters.
            width (int): Represents the width of two opposing sides of 
                the Rectangle in centimeters.

        Raises:
            ValueError: Raises a ValueError when length or width is not
                numeric.
        """

        super().__init__(color)

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")

        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")

        self.__length = length
        self.__width = width

    def calculate_area(self) -> float:
        """Calculates and returns the area of the rectangle.
        
        Returns:
            The area of the rectangle.
        """

        area = self.__length * self.__width
        return area
    
    def calculate_perimeter(self) -> float:
        """Calculates and returns the perimeter of the rectangle.
        
        Returns:
            The perimeter of the rectangle.    
        """

        perimeter = self.__length * 2 + self.__width * 2
        return perimeter

    def __str__(self):
        """Returns a "informal" string representation of 
        the Rectangle object.
        
        Returns:
            str: The "informal" string representation of
            the Rectangle object.
        """
        shape_str = super().__str__()

        return (f"{shape_str} \n"
                f"This rectangle has four sides with the lengths of "
                f"{self.__length}, {self.__width}, {self.__length} " 
                f"and {self.__width} centimeters.")
    