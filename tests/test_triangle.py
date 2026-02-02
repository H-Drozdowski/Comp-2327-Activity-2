"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

import unittest
from shape.triangle import Triangle

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

class TestTriangle(unittest.TestCase):
    """Test for the Triangle class."""

    def test_init_initializes_state(self):
        """Tests if init is initialized correctly when the correct
        values are input."""

        #Arrange 
        color = "Blue"
        side_1 = 5
        side_2 = 5
        side_3 = 5

        #Act
        target = Triangle(color, side_1, side_2, side_3)

        #Assert
        self.assertEqual(color, target._color)
        self.assertEqual(side_1, target._Triangle__side_1)
        self.assertEqual(side_2, target._Triangle__side_2)
        self.assertEqual(side_3, target._Triangle__side_3)

    def test_init_exception_when_color_blank(self):
        """Tests if an exception is raised properly when a blank string
        is input into color."""

        #Arrange
        color = "   "
        side_1 = 5
        side_2 = 5
        side_3 = 5

        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = Triangle(color, side_1, side_2, side_3)

        #Assert
        expected = "Color cannot be blank."
        actual = str(exception_context.exception)

        self.assertEqual(expected, actual)
    
    def test_init_exception_when_side_1_not_numeric(self):
        """Tests if exception is raised properly when side_1 is not a
        integer."""

        #Arrange
        color = "Blue"
        side_1 = "Invalid Input"
        side_2 = 5
        side_3 = 5

        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = Triangle(color, side_1, side_2, side_3)

        #Assert
        expected = "Side 1 must be numeric."
        actual = str(exception_context.exception)

        self.assertEqual(expected, actual)

    def test_init_exception_when_side_2_not_numeric(self):
        """Tests if exception is raised properly when side_2 is not a
        integer."""

        #Arrange
        color = "Blue"
        side_1 = 5
        side_2 = "Invalid Input"
        side_3 = 5

        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = Triangle(color, side_1, side_2, side_3)

        #Assert
        expected = "Side 2 must be numeric."
        actual = str(exception_context.exception)

        self.assertEqual(expected, actual)

    def test_init_exception_when_side_3_not_numeric(self):
        """Tests if exception is raised properly when side_3 is not a
        integer."""

        #Arrange
        color = "Blue"
        side_1 = 5
        side_2 = 5
        side_3 = "Invalid Input"

        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = Triangle(color, side_1, side_2, side_3)

        #Assert
        expected = "Side 3 must be numeric."
        actual = str(exception_context.exception)

        self.assertEqual(expected, actual)
    
    def test_str_returns_string_representation(self):
        """Tests that str returns the correct string 
        representation."""

        #Arrange
        color = "Blue"
        side_1 = 5
        side_2 = 5
        side_3 = 5

        #Act
        target = Triangle(color, side_1, side_2, side_3)
        actual = target.__str__()

        #Assert
        expected = (
            "This triangle has three sides with lengths of 5, 5, and "
            "5 centimeters.")


        self.assertEqual(expected, actual)

    def test_calculate_area_returns_correct_calculated_value(self):
        """Tests that calculate_area returns the area of the triangle
        correctly."""

        #Arrange
        color = "Blue"
        side_1 = 5
        side_2 = 5
        side_3 = 5

        #Act
        target = Triangle(color, side_1, side_2, side_3)
        actual = round(target.calculate_area(), 2)

        #Assert
        expected = 10.83

        self.assertEqual(expected ,actual)

    def test_calculate_perimeter_returns_correct_calculated_value(self):
        """Tests that calculate_perimeter returns the correct perimeter
        of the triangle."""

        #Arrange
        color = "Blue"
        side_1 = 5
        side_2 = 5
        side_3 = 5

        #Act
        target = Triangle(color, side_1, side_2, side_3)
        actual = target.calculate_perimeter()

        #Assert
        expected = 15
        
        self.assertEqual(expected, actual)
        