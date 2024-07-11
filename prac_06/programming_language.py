class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance.
        name: str, the name of the programming language
        typing: str, the typing nature of the language (Static/Dynamic)
        reflection: bool, whether the language supports reflection
        year: int, the year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


