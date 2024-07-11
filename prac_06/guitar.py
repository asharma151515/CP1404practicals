class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.
        name: str, the name of the guitar
        year: int, the year the guitar was made
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year):
        """Calculate how old the guitar is in years."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Check if the guitar is vintage (50 or more years old)."""
        return self.get_age(current_year) >= 50


