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

print(f"Random number from randint(5, 20): {random_number1}")
print(f"Random number from randrange(3, 10, 2): {random_number2}")
print(f"Random number from uniform(2.5, 5.5): {random_number3}")

# Generating a random number between 1 and 100 (inclusive)
random_number4 = random.randint(1, 100)
print(f"Random number between 1 and 100 inclusive: {random_number4}")
