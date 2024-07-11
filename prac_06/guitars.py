from guitar import Guitar


def main():
    guitars = []

    print("My Guitars!")

    while True:
        name = input("Name: ")
        if not name:
            break

        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{name} ({year}) : ${cost:.2f} added.")

    print("\nGuitars!")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f}{vintage_string}")


if __name__ == "__main__":
    main()
