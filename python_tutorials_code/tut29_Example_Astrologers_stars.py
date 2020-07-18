# pattern parinting
# input=Integer n
# boolean=True or false
# true
# *
# **
# ***
# ****
# false
# ****
# ***
# **
# *
n = int(input("Enter Number: "))
boolnum = int(input("Enter 1 or 0:\nif you Enter 1 then pattern print in acceding order\nif you Enter 0 then "
                    "pattern print descending order\n"))
if boolnum ==1:
    for i in range(n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
elif boolnum ==0:
    for i in range(n, -1, -1):
        for j in range(i):
            print("*", end=" ")
        print()
else:
    print("you Enter Invalid Input!!!!!")
