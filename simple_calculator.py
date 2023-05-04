import math

def calculator(num1, num2, operator):
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == 'sqrt':
            if num1 < 0:
                raise ValueError("Cannot take square root of negative number")
            result = math.sqrt(num1)
        else:
            raise ValueError("Invalid operator")
    except Exception as e:
        print("Error:", e)
    else:
        return result

# take user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, **, sqrt): ")

# calculate the result
result = calculator(num1, num2, operator)

# display the result
if result is not None:
    print("Result:", result)
