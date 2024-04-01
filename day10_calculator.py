def format_name(f_name,l_name):
  a= f_name.title()
  b=l_name.title()
  return a+b
print(format_name('VANSHIKA',' saxena'))

##calculator 
# Define the arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Create a dictionary mapping operators to the corresponding functions
operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    
    
    # Get user input for numbers and the operation
    num1 = float(input("What's the first number? : "))
    num2 = float(input("What's the second number? : "))

    # Print available operations
    for key in operation:
        print(key)

    # Get user input for the desired operation
    opp = input("Which of the following operations do you want to perform? ")

    # Retrieve the function corresponding to the selected operation
    function = operation[opp]
    first_ans = function(num1, num2)
    print(f"{num1} {opp} {num2} = {first_ans}")

    ans = True
    while ans:
        a = input(f"Type 'y' to continue calculating with {first_ans}, or type 'n' to exit: ")
        if a == 'n':
            ans = False
            calculator()
        else:
            opp = input("Pick another operation: ")
            num3 = float(input("What's the next number? : "))
            function = operation[opp]
            second_ans = function(first_ans, num3)
            print(f"{first_ans} {opp} {num3} = {second_ans}")
            first_ans = second_ans
