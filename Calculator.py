num1 = int(input("Enter first number \n"))
operator = input("Chose operator + , - , * , /\n")
num2 = int(input("Enter the second number \n"))

def Calculator(num1 , num2 , num3):
    total = 0
    while True: 
       
        if (operator =="+" ):
         total = num1 + num2
         print(f'Sum of two number are {total}')
         break
        elif(operator =="-" ):
           total = num1 - num2
           print(f'Subtraction of two number are {total}')
           break
        elif(operator =="*"):
           total = num1 * num2
           print(f'Multiplication of two number are {total}')
           break
        elif(operator =="/"):
           total = num1 / num2
           print(f'Division of two number are {total}')
           break
Calculator()      
           
        
    
