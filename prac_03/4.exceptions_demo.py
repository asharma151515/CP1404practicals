"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: A ValueError will occur if the user enters a non-integer
value when prompted to enter the numerator or denominator.
For example, entering a string instead of a number.
-----------------------------------------------------------------
2. When will a ZeroDivisionError occur?
Answer: A ZeroDivisionError will occur
if the user enters 0 as the denominator, which
leads to division by zero.
-----------------------------------------------------------------
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes, to avoid the possibility of a ZeroDivisionError, which can add a check
before performing the division operation to ensure that the denominator is not zero. If the denominator
is zero, which can prompt the user to enter a valid non-zero denominator.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")