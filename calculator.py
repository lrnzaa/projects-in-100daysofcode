# Simple Calculator Program

def add(num1, num2):
    return num1 + num2

def subs(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def main():
    while True:
        print()
        print("Simple Calculator Program")
        print("--------------------------")
        print("Operations:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("--------------------------")
        print("To exit, enter 5")

        op = input("Select operations: ")

        if op == "5":
            break

        print("Enter two numbers.")
        firstNum = int(input("First number: ")) 
        secNum = int(input("Second number: "))

        print("Processing...")

        operation = ''
        result = 0

        if op == "1":
            operation = "addition"
            result = add(firstNum, secNum)
        elif op == "2":
            operation = "substraction"
            result = subs(firstNum, secNum)
        elif op == "3":
            operation = "multiplication"
            result = multi(firstNum, secNum)
        elif op == "4":
            operation = "division"
            result = div(firstNum, secNum)

        print("Result of the " + operation + " between " + str(firstNum) + " and " + str(secNum) + " is " + str(result) + ".")

if __name__ == "__main__":
    main()