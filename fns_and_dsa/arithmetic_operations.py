from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()def perform_operation(num1,num2,operation):
    if operation == "add":
       return num1+num2
    elif  operation == "subtract":
          return num1-num2  
    elif  operation == "multiply":
          return num1*num2  
    elif  operation == "divide":
          return num1/num2
          else:
               num2\s==\s0:
             return("Zero can not be a dinomenator")   

     



# Define a function named perform_operation.
# Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
# The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
# For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
# # Return the result of the arithmetic operation. 
# num1=float(input("Enter your first number"))
#     num2=float(input("Enter your second number"))   
