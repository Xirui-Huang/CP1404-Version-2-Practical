"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.
    >>> repeat_string("Python", 1)
    'Python'
    >>> repeat_string("hi", 2)
    'hi hi'
    """
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def run_tests():
    """Run the tests on the functions."""
    # Assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python", "repeat_string does not handle single repetition correctly"
    # This test should now pass with the corrected function
    assert repeat_string("hi", 2) == "hi hi", "repeat_string does not separate repeated strings with spaces"

    # Testing Car's odometer initialization
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Testing Car's fuel initialization
    test_car_default_fuel = Car()
    assert test_car_default_fuel.fuel == 0, "Car fuel should default to 0 if not specified"

    test_car_with_fuel = Car(fuel=10)
    assert test_car_with_fuel.fuel == 10, "Car fuel is not set correctly when specified"

def format_as_sentence(phrase):
    """
    Formats the given phrase as a sentence starting with a capital letter and ending with a single full stop.
    >>> format_as_sentence("hello")
    'Hello.'
    >>> format_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_as_sentence("well done")
    'Well done.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]

# Uncomment the following line to enable the doctest to run
doctest.testmod()

# Run the regular tests
run_tests()

