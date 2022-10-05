# Addition
def add(a,b):
    return '\nAdditon of {} + {} : {}'.format(a, b, a + b)

# Subtraction
def subtract(a, b):
    return '\nSubtraction of {} - {} : {}'.format(a, b, a - b)

# Multiplication
def multiply(a, b):
    return  '\nMultiplication of {} X {} : {}'.format(a, b, a * b)

# Division
def divide(a, b):
    c = float(a)
    d = float(b)
    return '\nDivision of {} by {} : {}'.format(a, b, c / d)

# Modulus
def mod(a, b):
    return '\nModulus : {}'.format(a % b)

# MAIN
num1=int(input("\nEnter the first number: "))
num2=int(input("Enter the second number: "))
while True:
    print("\nChoose the operator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    ch = int(input("\nEnter your operator: "))
    if ch == 1:
        print(add(num1, num2))
    elif ch == 2:
        print(subtract(num1,num2))
    elif ch == 3:
        print(multiply(num1,num2))
    elif ch == 4:
        print(divide(num1,num2))
    elif ch == 5:
        print(mod(num1,num2))
    elif ch == 6:
        print("\nExiting.....\n")
        break
    elif ch > 6 or ch < 0:
        print("\nInvalid operator")
    else:
        print("\nInvalid operator")
