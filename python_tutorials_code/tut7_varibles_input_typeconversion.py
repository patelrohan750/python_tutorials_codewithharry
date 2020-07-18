# datavaribles,input,typeconversion
var1 = "Hello friends "
var2 = "20"
var = 5
var3 = 6
va = 5.678
print(var1)
print(type(var1))
print(type(var2))
print(type(var3))
print(type(va))
print("sum is", var + var3)
print("sum is", var3 + va)
print(10 * (str(var3) + str(var)), end='\n')

'''
3 type coversion
str()
int()
float()
'''
print("sum of", int(var2) + var)
print("string add", var1 + var2)
print("string and int", var1 + str(var))
print(10 * "hello\n")
# take input from user
print("Enter 1st number")
num1 = input()
print("Enter 2nd number")
num2 = input()
print("sum is", int(num1) + int(num2))
