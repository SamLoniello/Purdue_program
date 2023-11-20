def add_numbers(a, b):
    return a + b

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = add_numbers(num1, num2)
    print("The result of adding", num1, "and", num2, "is:", result)

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(2.5, 3.5) == 6.0

if __name__ == "__main__":
    main()
    test_add_numbers()
    print("All tests passed!")
