def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print("Temperature Converter")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius * 9 / 5 + 32
            print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print("Temperature in Celsius: {:.2f}".format(celsius))
        else:
            print("Invalid option. Please try again.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Program terminated.")

if __name__ == '__main__':
    main()