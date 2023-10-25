def calculate_sum(*args):

    result = 0
    for num in args:
        result += num
    return result
  # Example usage:
result = calculate_sum(5, 10, 2.5, 7)
print("Sum:", result)  
