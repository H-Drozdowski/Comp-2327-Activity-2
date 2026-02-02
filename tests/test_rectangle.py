"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""
from shape.rectangle import Rectangle 
import unittest

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

class TestRectangle(unittest.TestCase):
    """Test fot the rectangle class"""

    def test_init_initializes_state(self):
        """Tests if Rectangle is initialized correctly when the correct
        values are input."""

        #Arrange 
        color = "Blue"
        length = 5
        width = 5

        #Act
        target = Rectangle(color, length, width)

        #Assert
        self.assertEqual(color, target._color)
        self.assertEqual(length, target._Rectangle__length)
        self.assertEqual(width, target._Rectangle__width)

    def test_init_exception_when_color_blank(self):
        """Tests if an exception is raised properly when a blank string
        is input into color."""

        #Arrange 
        color = "   "
        length = 5
        width = 5

        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = Rectangle(color, length, width)

        #Assert
        expected = "Color cannot be blank."
        actual = str(exception_context.exception)

        self.assertEqual(expected, actual)

    def test_init_exception_when_length_not_numeric(self):
        """Tests if exception is raised properly when length is not a
        integer."""

        #Arrange 
        color = "Blue"
        length = "Invalid Input"
        width = 5

        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = Rectangle(color, length, width)

        #Assert
        expected = "Length must be numeric."
        actual = str(exception_context.exception)

        self.assertEqual(expected, actual)

    def test_init_exception_when_width_not_numeric(self):
        """Tests if exception is raised properly when width is not a
        integer."""

        #Arrange 
        color = "Blue"
        length = 5
        width = "Invalid Input"

        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = Rectangle(color, length, width)

        #Assert
        expected = "Width must be numeric."
        actual = str(exception_context.exception)

        self.assertEqual(expected, actual)

    def test_str_returns_string_representation(self):
        """Tests that str returns the correct string 
        representation."""

        #Arrange 
        color = "Blue"
        length = 5
        width = 5

        #Act
        target = Rectangle(color, length, width)

        #Assert
        expected = ("The shape color is Blue. \n" 
                    "This rectangle has four sides with the lengths of "
                    "5, 5, 5 and 5 centimeters.")
        actual = target.__str__()

        self.assertEqual(expected, actual)

    def test_calculate_area_returns_correct_calculated_value(self):
        """Tests that calculate_area returns the area of the Rectangle
        correctly."""

        #Arrange
        color = "Blue"
        length = 5
        width = 5

        #Act
        target = Rectangle(color, length, width)

        #Assert 
        expected = 25
        actual = target.calculate_area()

        self.assertEqual(expected, actual)

    def test_calculate_perimeter_returns_correct_calculated_value(self):
        """Tests that calculate_perimeter returns the correct perimeter
        of the Rectangle."""

        #Arrange
        color = "Blue"
        length = 5
        width = 5

        #Act
        target = Rectangle(color, length, width)

        #Assert
        expected = 20
        actual = target.calculate_perimeter()

        self.assertEqual(expected, actual)

