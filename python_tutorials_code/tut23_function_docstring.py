# functions and docstring
# docstring --docstring use in function that denotes main functionality of function
# a=5
# b=10
# c=sum((a,b))  #inbuilt function
# print(c)


def function1(a, b):
    print("hello function1 is calling......", a + b)


def function2(a, b):
    """this function will calculate Average of two numbers"""
    average = (a + b) / 2
    return average


function1(10, 20)
var = function2(7, 5)
print(var)
print(function2.__doc__)
