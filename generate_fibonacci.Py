def calculate_sum(*args):
    result = 0  # Initialize the result to zero
    for num in args:
        result += num  # Add each argument to the result
    return result

# Example usage:
result = calculate_sum(5, 10, 2.5, 7)
print("Sum:", result)  # Output: Sum: 24.5
