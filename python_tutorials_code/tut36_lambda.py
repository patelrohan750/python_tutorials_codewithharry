def sum(a,b):
    return a+b

print(sum(10,5))

minus=lambda x,y:x-y
print(minus(15,10))

list1=[[1, 14], [5, 6], [8,23]]
list1.sort(key=lambda x:x[1])
print(list1)