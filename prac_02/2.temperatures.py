def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def display_menu():
    print("MENU:")
    print("C - Convert Celsius to Fahrenheit")
    print("F - Convert Fahrenheit to Celsius")
    print("Q - Quit")

def main():
    display_menu()
    choice = input("Enter your choice: ").upper()

    while choice != 'Q':
        if choice == 'C':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        elif choice == 'F':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        else:
            print("Invalid choice. Please try again.")

        display_menu()
        choice = input("Enter your choice: ").upper()

    print("Thank you for using the temperature converter.")

if __name__ == "__main__":
    main()