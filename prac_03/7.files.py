# Question 1
# Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Question 2
# Read the name from "name.txt" and print a greeting
with open('name.txt', 'r') as file:
    name = file.read()
print(f"Hi {name}!")

# Question 3
# Create a text file called numbers.txt with numbers 17, 42, 400 on separate lines
with open('numbers.txt', 'w') as file:
    file.write("17\n42\n400\n")

# Read the first two numbers from numbers.txt, add them, and print the result
with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
result = number1 + number2
print(f"The sum of the first two numbers is: {result}")

# Question 4
# Print the total for all lines in numbers.txt
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print(f"The total sum of all numbers in the file is: {total}")