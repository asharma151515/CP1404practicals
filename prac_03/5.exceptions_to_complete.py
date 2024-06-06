"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

"""
1.The program will continuously prompt the user to enter a valid integer until a valid integer is provided.
2.The ValueError exception is added to catch non-integer inputs, ensuring the program does not crash when a non-number is entered.
3.The is_finished flag is set to True when a valid integer is entered, allowing the program to exit the loop.
4.The print("Valid result is:", result) statement is placed outside the loop to display the valid integer entered by the user after the loop exits.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        is_finished = True  # Set is_finished to True to exit the loop when a valid integer is entered

print("Valid result is:", result)