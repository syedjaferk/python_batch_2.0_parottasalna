def get_operator():
    print("Simple Calculator")
    print("\tSelect operation")
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print("\t5. Modulus")
    print("\t6. Power")
    return int(input("Enter number for operation "))

def get_operands():
    a_num = float(input("Enter first  number "))
    b_num = float(input("Enter second number "))
    return a_num, b_num

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(a, b):
    return a ** b

def rem(a, b):
    return a % b

def calculate(op, a, b):
    if op == 1:
        result = add(a, b)
    elif op == 2:
        result = sub(a, b)
    elif op == 3:
        result = mul(a, b)
    elif op == 4:
        result = div(a, b)
    elif op == 5:
        result = a % b
    else:
        result = a ** b
    return result

def calculator():
    op = get_operator()
    a, b = get_operands()
    print("Result:", calculate(op, a, b))

    