#Calculator Program in python by defining operations
# Define Operators or Functions: Addition, Subtraction, Multiplication, and Division
# Addition
def addition(n1, n2):
    return n1 + n2

# Subtraction
def subtraction(n1, n2):
    return n1 - n2
# Multiplication
def multiplication(n1, n2):
    return n1 * n2
# Division
def division(n1, n2):
    return n1 / n2
print("Select Operations")
print("1. Addition","2. Subtraction""3. Multiplication""4. Division")
# Giving the option to the user to choose the operation
operation = int(input("Enter choice of operation 1/2/3/4: "))
#Taking Input from the Users
n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))
# Apply Conditional Statements: To make operation as-per-user choices
if operation == 1:
    print (n1, "+", n2, "=", addition(n1, n2))
elif operation == 2:
    print (n1, "-", n2, "=", subtraction(n1, n2))
elif operation == 3:
    print (n1, "*", n2, "=", multiplication(n1, n2))
elif operation == 4:
    print (n1, "/", n2, "=", division(n1, n2))
else:
    print("Invalid Input")
