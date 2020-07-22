x = 20  # global variable


def function1(n):
    # x = 5  # local variable
    m = 10  # local variable
    global x
    x = x + 5
    print(x, m)
    print(n, "function1 is calling....")


function1("hello")
print(x)

# y = 25
#
#
# def fun1():
#     y = 20
#
#     def fun2():
#         global y
#         y = y + 5
#         print("fun2 calling", y)
#
#     fun2()
#     print(y)
#
#
# fun1()
# print(y)
