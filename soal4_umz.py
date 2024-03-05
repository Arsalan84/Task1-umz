flag=int(input("please enter number(1-farenhiet to celsios 2-celsios to farenhiet :)"))
if flag==1:
    temp_f=float(input("please enter your temperature: "))
    print((temp_f-32)*5/9)
elif flag==2:
    temp_c=float(input("please enter your temperature:")) 
    print((1.8*temp_c)+32)
else:
    print("invalid value")       