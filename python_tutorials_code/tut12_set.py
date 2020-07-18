# set contain unique value
# s={1,2,3,4}
# print(s)
# print(type(s))

# second way
# l=[1,2,3,4,5]
# s1=set(l)
# print(s1)
s2=set()
s2.add(1)
s2.add(2)
s2.add(3)
# s2.add(3)
s3=s2.union({1,2,5})
# s3=s2.intersection({1,2,5})
# print(s2,s3)
s2.remove(2)
s2.isdisjoint()
print(s2)
