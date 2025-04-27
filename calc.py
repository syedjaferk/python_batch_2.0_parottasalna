def get_operator():
    print("Welcome to the Calculator !")
    print("Select Operation ")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    operator = int(input("Enter your operator : "))
    return operator

def get_operands():
    num1 = int(input("Enter the value of number 1 "))
    num2 = int(input("Enter the value of number 2 "))
    return num1, num2

def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def sub(num1, num2):
    return num1 - num2

def modulus(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

def calculate(op, num1, num2):
    if op == 1:
        return add(num1, num2)
    elif op == 2:
        return sub(num1, num2)
    elif op == 3:
        return mul(num1, num2)
    elif op == 4:
        return div(num1, num2)
    elif op == 5:
        return modulus(num1, num2)
    elif op == 6:
        return power(num1, num2)



def calculator():
    try:
        op = get_operator()
        a, b = get_operands()
        result = calculate(op, a, b)
        print("Your result is ", result)
    except ValueError as ve:
        print("Please check the input value you entered", str(ve))
    except ZeroDivisionError as zde:
        print("Division by Zero is not possible, Please check your input")


while True:
    calculator()