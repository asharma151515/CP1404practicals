def main():
    """
    This function contains the main logic of the program.
    """
    numbers = [3, 1, 4, 1, 5, 9, 2]

# Display the values of the expression
    print(numbers[0])
    print(numbers[-1])
    print(numbers[3])
    print(numbers[:-1])
    print(numbers[3:4])
    print(5 in numbers)
    print(7 in numbers)
    print("3" in numbers)
    print(numbers + [6, 5, 3])

# Change the first element of number to "ten"
    numbers[0] = "ten"

# Change the last elemet of number to 1
    numbers[-1] = 1

# Print all elements from numbers except the first two
    print(numbers[2:])


# Print whether 9 is an element of number
    print(9 in numbers)

if __name__ == "__main__":
    main()
