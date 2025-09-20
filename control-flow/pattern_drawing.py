# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after finishing a row
    row += 1
