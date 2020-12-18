# making a calculator:
def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("############")
print("Make a choice:")
print("############")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
print("############")
choice = int(input("Enter your choice here: "))
result = 0
while choice != 5:
    if choice == 1:
       result = add(num1, num2)
    if choice == 2:
        result = subtract(num1, num2)
    if choice == 3:
        result = multiply(num1, num2)
    if choice == 4:
        result = divide(num1, num2)
    print("Total is: ", result)
    choice = int(input("Enter your choice here: "))
    num2 = float(input("Enter a new number: "))
    num1 = result
