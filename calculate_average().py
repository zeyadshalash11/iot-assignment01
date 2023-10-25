def calculate_average(*args):
    if not args:
        return 0  # Return 0 if no arguments are provided to avoid division by zero.
    
    total = sum(args)  # Calculate the sum of the numbers.
    average = total / len(args)  # Calculate the average.
    return average

# Example usage:
numbers = [5, 10, 15, 20]
average = calculate_average(*numbers)
print("Average:", average)  # Output: Average: 12.5
