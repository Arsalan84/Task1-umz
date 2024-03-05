num1=float(input("please enter first number:"))
num2=float(input("please enter second number:"))
operation=input("please enter your operation (sum,difference,multiply,divide):")
if operation=="sum":
    print(num1+num2)
elif operation=="difference":
    print(num1-num2)
elif operation=="multiply":
    print(num1*num2)
elif operation=="divide":
    if num2==0:
        print("it is not divided")
    else: 
        print(num1/num2)
else:    
    print("your operation invalid")    