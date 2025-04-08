def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swapping without a third variable
    x, y = y, x
    print(f"Swapped: x = {x}, y = {y}")

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Test case 1: Non-numeric input
result1 = swap("Apple", 10)
print("Returned:", result1)

# Test case 2: Numeric input
result2 = swap(9, 17)
print("Returned:", result2)


