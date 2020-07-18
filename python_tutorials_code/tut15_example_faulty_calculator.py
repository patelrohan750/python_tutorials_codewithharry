# Exrersice:2  faulty calculator
# 45 * 3 = 555, 56 + 9 = 77,56/6 = 4
# Design a calculator wich will correctly solve all the problem exexpt
# the following ones:
# 45 * 3 = 555, 56 + 9 = 77,56/6 = 4
# your program should take operator and the two numbers as input from the user
# and then return result

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
op=input("select operator like: +, * , - , / :::")
if op=="+" and num1 ==56 and num2 ==9:
    print("77")
elif op=="+":
    print(num1 + num2)
elif op=="-":
    print(num1-num2)
elif op=="*" and num1==45 and num2 == 3:
    print("555")
elif op=="*":
    print(num1 * num2)
elif op=="/" and num1==56 and num2==6:
    print("4")
elif op=="/":
    print(float(num1 / num2))
else:
    print("you enter wrong choice..........")