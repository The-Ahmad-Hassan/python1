a = 3
b=4.3
c="4+j"
print(a,b,c)
print(type(a))

print(type(b))

#Checks number is even or odd

no=int(input("Enter the no : "))

if no%2==0:
    print("NO is even")
else:
    print("NO is odd")


#claculate the factorial
result = 1
fact=int(input("Enter the number : " ))

for i in range(1,fact+1):
     result=result*i 


print("The factorial of ", fact , "is : " , result)



  