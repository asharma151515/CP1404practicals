class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic  # New field for Pointer Arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"