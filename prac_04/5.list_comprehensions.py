"""
CP1404 Practical
List Comprehensions
"""

# List of strings
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# List comprehension that creates a new list containing the first letter of each name
first_initials = [name[0] for name in names]
print("First initials:", first_initials)

# List comprehension that creates a list containing the initials
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print("Full initials:", full_initials)

# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print("Lowercase full names:", lowercase_full_names)

# List comprehension to create a list of integers from the list of strings
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(num) for num in almost_numbers]
print("Numbers:", numbers)

# List comprehension to create a list of only the numbers that are greater than 9 from the numbers
greater_than_9 = [num for num in numbers if num > 9]
print("Numbers greater than 9:", greater_than_9)

# List comprehension to create a string (not list) of the last names for those full names longer than 11 characters
long_full_names = [name.split()[1] for name in full_names if len(name) > 11]
long_last_names_str = ', '.join(long_full_names)
print("Last names longer than 11 characters:", long_last_names_str)



