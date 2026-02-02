"""This module defines the Triangle class."""

from shape.shape import Shape
from math import sqrt

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

class Triangle(Shape):

    def __init__(self, color : str, side_1 : int,
                 side_2 : int, side_3 : int):
        """Initializes a new instance of the Triangle class.
        
            Args:
                color (str): Represents the color of the shape.
                side_1 (int) Represents the length of the first side of 
                the Triangle in centimeters.:
                side_2 (int): Represents the length of the second side 
                of the Triangle in centimeters.
                side_3 (int): Represents the length of the third side of
                the Triangle in centimeters.

            Raises:
                ValueError: A value error is raised when one of the 
                sides of the triangle is not a numeric value. A 
                ValueError is also raised when the side of the triangle
                do not satisfy the Triangle Inequality Theorem.
        """
        super().__init__(color)

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")

        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")
        
        if not ((side_1 + side_2) > side_3 and (side_1 + side_3)> side_2
            and(side_2 + side_3) > side_1):

            raise ValueError(f"The sides do not satisfy the Triangle"
                             f"Inequality Theorem.")

        
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3


    def calculate_area(self) -> float:
        """Calculates the area of the triangle.
        
        Returns: 
            The area of the triangle.
        """

        sp = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = sqrt(sp * (sp - self.__side_1) * (sp - self.__side_2) 
                       * (sp - self.__side_3))
        
        return area
    
    def calculate_perimeter(self) -> float:
        """Calculates the perimeter of the triangle.
        
        Returns:
            The perimeter of the triangle.
        """

        perimeter = (self.__side_1 + self.__side_2 +self.__side_3)

        return perimeter

    def __str__(self) -> str:
        return (f"The shape color is {self._color}\n"
                f"This triangle has three sides with lengths of "
                f"{self.__side_1}, {self.__side_2}, and {self.__side_3}"
                f" centimeters.")