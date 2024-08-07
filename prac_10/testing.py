
"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""
import doctest
from prac_06.car import Car  # Assuming you have a Car class in this module


def repeat_string(s, n):
    """
    Repeat string s, n times, with spaces in between.

    >>> repeat_string("Python", 1)
    'Python'
    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("yo", 3)
    'yo yo yo'
    """
    return ' '.join([s] * n)  # Fixed to join the repeated string with spaces


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
    return len(word) >= length  # Fixed to include equal length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.

    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    return phrase.capitalize() + '.'  # Capitalize and add a full stop


def run_tests():
    """Run the tests on the functions."""
    # Assert test for repeat_string
    assert repeat_string("Python", 1) == "Python", "Test failed!"
    assert repeat_string("hi", 2) == "hi hi", "Test failed!"
    assert repeat_string("yo", 3) == "yo yo yo", "Test failed!"

    # Assert tests for Car class fuel setting
    test_car_default = Car()  # Assuming default fuel is set in the Car class
    assert test_car_default._fuel == 0, "Car does not set default fuel correctly"

    test_car_custom = Car(fuel=10)
    assert test_car_custom._fuel == 10, "Car does not set custom fuel correctly"

    print("All tests passed!")


if __name__ == "__main__":
    doctest.testmod()  # Uncommented to run doctests
    run_tests()  # Run the assertion tests
