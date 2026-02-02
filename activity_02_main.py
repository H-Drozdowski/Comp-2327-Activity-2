""""A client program written to verify correctness of the activity 
classes.
"""
from shape import *

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """

    # 1. Declare variable that would store a list of Shape objects.
    # Initialize the variable to an empty list.

    shape_list = []

    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.


    try:
        triangle = Triangle("Red", 5, 5, 5)
        shape_list.append(triangle)

    except ValueError as exception:
        print(str(exception))

    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.

    try:
        rectangle = Rectangle("Blue", 5, 5)
        shape_list.append(rectangle)

    except ValueError as exception:
        print(str(exception))

    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    
    try:
        rectangle_2 = Rectangle("Pink", 4, 5)
        rectangle_3 = Rectangle("Yellow", 5, 8)
        triangle_2 = Triangle("Light Blue", 4, 6, 6)

        shape_list.append(rectangle_2)
        shape_list.append(rectangle_3)
        shape_list.append(triangle_2)

    except ValueError as exception:
        print(str(exception))
        
    # 5. Iterate through the list of shapes.  
    # On each iteration:
    # - Print the string representation of the shape.
    # - Print the area of the shape to 2 decimal places.
    # - Print the perimeter of the shape to 2 decimal places.

    for shape in shape_list:

        try:
            print(shape)
            print(round(shape.calculate_area(), 2))
            print(round(shape.calculate_perimeter(), 2))

        except ValueError as exception:
            print(str(exception))


if __name__ == "__main__":
    main()
