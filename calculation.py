print("----Calculation of Two integer---")
print("what operation you want to perform? \n1.Addition (+) \n2.Substraction (-) \n3.Multiplication (* \n4.Division (/)")


while True:
    a = int(input("Enter first digit: "))
    b = int(input("Enter second digit: ")) 
    
    cal = input("+,-,*,/: ")
    if cal == "+":
        c = a+b
        print(a,"+",b,"=",c)

    elif cal == "-":
        c = a-b
        print(a,"-",b,"=",c)
        
    elif cal == "*":
        c = a*b
        print(a,"*",b,"=",c)
        
        
    elif cal == "/":
        if b ==0:
          print("Sorry any number cannot be divide by zero(0)")
        else: 
            c = a/b
            print(a,"/",b,"=",c)
    
        
    else:
        print("Please! Enter a valid operation!!") 
        
    # ext = input("Enter 'Q' to exit or enter 'C' to contine ").lower()
    # if ext == "q":
    #   break

