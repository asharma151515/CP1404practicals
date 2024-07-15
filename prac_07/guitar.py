def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)
    guitars.sort()
    display_guitars(guitars)


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def is_vintage(self, current_year):
        """Check if the guitar is vintage based on the current year."""
        return current_year - self.year >= 50

def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header line
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)



if __name__ == "__main__":
    main()
