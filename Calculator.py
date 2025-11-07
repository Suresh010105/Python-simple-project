print("   Simple Calculator    ")
num1=int(input("Enter the first number= "))
num2=int(input("Enter the second number= "))

opr=input("Select operator(+ - * /)= ")

if opr==("+"):
    print(num1 + num2)
elif opr==("-"):
    print(num1-num2)
elif opr==("*"):
    print(num1*num2)
elif opr==("/"):
    if num2!=0:
        print(num1/num2)
    else:
        print("Dividing by zero is not possible")
else:
    print("Invalid operator or number")
    


