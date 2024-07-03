def perform_operation(num1,num2,operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = string(input("Enter the operation (add, subtract, multiply, divide): "))
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
         if __name__ == "__main__":
    main()
