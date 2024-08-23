import random as r
n=int(input("Enter length of password : "))
s=""
for i in range(n):
    s+=chr(r.randint(33,126))
print(s)