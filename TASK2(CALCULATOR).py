#TASK 2 CALCULATOR

#An Python program for simple calculator
 
#This Function is to add two numbers
def add(num1, num2):
    return num1 + num2
 
#This Function is to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
 
# This Function  is to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
#This Function is to divide two numbers
def divide(num1, num2):
    try:
          return num1/num2
    except ZeroDivisionError as e:##Exception handling :IF it is divided by zero
        print(e)
        return 0
        
print("Select the operation to be performed: -\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")
 
#Choosing the operation
operation = int(input("Select operations from 1, 2, 3, 4 :"))

#Getting two input values from the user
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

#based on the operation
if operation == 1:
    print("ADDITION : \n",num_1, "+", num_2, "=",add(num_1, num_2))
 
elif operation == 2:
    print("SUBTRACTION : \n",num_1, "-", num_2, "=",subtract(num_1, num_2))
 
elif operation == 3:
    print("MULTIPLICATION : \n",num_1, "*", num_2, "=",multiply(num_1, num_2))
 
elif operation == 4:
    print("DIVISION : \n",num_1, "/", num_2, "=",divide(num_1, num_2))
else:
    print("Invalid input")