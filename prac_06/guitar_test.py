from guitar import Guitar


def run_tests():
    # Create a Guitar object for testing
    test_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

    # Test get_age() method
    assert test_guitar.get_age(2022) == 100, "get_age() test failed"

    # Test is_vintage() method
    assert test_guitar.is_vintage(2022) == True, "is_vintage() test failed"

    print("All tests passed successfully.")


if __name__ == "__main__":
    run_tests()