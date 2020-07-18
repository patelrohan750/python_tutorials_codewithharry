f = open("tut26_test.txt", "rt")  # here we can use rb ,rt,etc

# content=f.read()
# print(content)

print(f.readlines())

# print(f.readline())
# print(f.readline())

# content=f.read(25555)
# print("1",content)

# content=f.read(2555555)
# print("2",content)

# for item in f:  # here when we can use print all content in loop then not use read() function
#     print(item,end=" ")


f.close()
