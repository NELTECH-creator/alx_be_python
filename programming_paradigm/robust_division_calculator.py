def safe_divide(numerator, denominator):
    """Safely perform division with error handling."""
    try:
        # Attempt to convert both inputs to floats
        num = float(numerator)
        den = float(denominator)

        try:
            # Try performing the division
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
