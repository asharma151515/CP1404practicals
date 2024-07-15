
from guitar import Guitar


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def main():
    guitars = load_guitars('guitars.csv')

    # Ask the user to enter new guitars
    while True:
        name = input("Enter the name of the guitar (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        year = int(input("Enter the year of the guitar: "))
        cost = float(input("Enter the cost of the guitar: "))
        guitars.append(Guitar(name, year, cost))

    # Display all guitars
    print("\nAll Guitars:")
    display_guitars(guitars)

    # Save all guitars to the data file
    save_guitars('guitars.csv', guitars)
    print("\nGuitars saved to file.")


if __name__ == "__main__":
    main()
