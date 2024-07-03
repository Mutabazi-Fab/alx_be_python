def perform_operation(num1,num2,operation):
    if operation == "add":
       return num1+num2
    elif  operation == "subtract":
          return num1-num2  
    elif  operation == "multiply":
          return num1*num2  
    elif  operation == "divide":
          if num2==0:
             return("Zero can not be a dinomenator") 
          else:
             return num1/num2  





# Define a function named perform_operation.
# Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
# The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
# For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
# # Return the result of the arithmetic operation. 
# num1=float(input("Enter your first number"))
#     num2=float(input("Enter your second number"))   
