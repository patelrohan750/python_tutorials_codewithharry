# Exception handling

num1=input("Enter Number1: ")
num2=input("Enter Number2: ")
try:
    print("sum is: ",int(num1)+int(num2))
except Exception as e:
    print(e)

print("this line is very important...")