class Book:
    """A class representing a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Constructor: initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: called when a Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
