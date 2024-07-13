# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main entry function
def main():
    num1 = float(input("Enter the first number: "))  # Using float to handle decimal inputs
    num2 = float(input("Enter the second number: "))

    result = add_numbers(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result}")

# Unit test function
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, -5) == -10
    assert add_numbers(100, 200) == 300
    print("All test cases passed!")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
