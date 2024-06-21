import random

# Using the dir() function to explore the random module
print(dir(random))

# Using the help() function to get information about the randint and randrange functions
help(random.randint)
help(random.randrange)

# Generating random numbers using random.randint(), random.randrange(), and random.uniform()
random_number1 = random.randint(5, 20)  # line 1
random_number2 = random.randrange(3, 10, 2)  # line 2
random_number3 = random.uniform(2.5, 5.5)  # line 3

# random integer between 5 and 20(inclusive) busing the 'random.randint()'
print(f"Random number from randint(5, 20): {random_number1}")

# random number between 3 and 10 (Exclusive) stepping by 2 using 'random.randrange()'
print(f"Random number from randrange(3, 10, 2): {random_number2}")

# random float between 2.5 and 5.5 using 'random.uniform()'
print(f"Random number from uniform(2.5, 5.5): {random_number3}")

# Generating a random number between 1 and 100 (inclusive)
random_number4 = random.randint(1, 100)
print(f"Random number between 1 and 100 inclusive: {random_number4}")
