def format_digits(digits):
    # Ensure the input is a string of exactly 10 digits
    if len(digits) != 10 or not digits.isdigit():
        return "Invalid input. Please provide a string of exactly 10 digits."

    # Break the string into five parts of two digits each
    parts = [digits[i:i+2] for i in range(0, 10, 2)]
    
    # Create the formula string
    sum_parts = "+".join(parts)
    result = sum(int(part) for part in parts) / 5  # Calculate the average
    formula = f"({sum_parts})/5 = {result}"
    
    return formula

# Example usage
input_digits = "4150304530"

formatted_string = format_digits(input_digits)
print(formatted_string)
