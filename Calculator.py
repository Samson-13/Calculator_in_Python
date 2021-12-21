print("***Calculator***")
def add(a,b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return  a*b
def divide(a, b):
    return a/b


x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
print("Choose the operator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
ch=int(input("Enter your operator: "))
if ch== 1:
    print(add(x, y))
elif ch== 2:
    print(subtract(x,y))
elif ch== 3:
    print(multiply(x,y))
elif ch== 4:
    print(divide(x,y))
else:
    print("Unknown operator...")

