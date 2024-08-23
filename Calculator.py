print("Operators :\n'+' for ADDITION \n'-' for SUBTRACTION\n'*' for MULTIPLICATION\n'/' for DIVISION \n")
n1,n2=map(int,input("Enter numbers : ").split(" "))
oper=input("Provide Operation : ")
exp=str(n1)+oper+str(n2)
if oper=="+":
    a=(n1+n2)
elif oper=='-':
    a=(n1-n2)
elif oper=='*':
    a=n1*n2
elif oper=="/":
    a=n1/n2
print('\n',exp,' = ',a)