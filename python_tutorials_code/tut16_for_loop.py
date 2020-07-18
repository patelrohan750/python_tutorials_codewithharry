# for loop
# list1=["Rohan","Pokar","Rahul","jaydeep"]
# print(list1)
#
# for items in list1:
#     print(items)

# list2=[["rohan",26],["pokar",19],["rahul",24],["Jaydeep",20]]
# print(list2)
# for i,j in list2:
#     print(i,"roll Number is: ",j)

# dict1=dict(list2)
# print(dict1)
# for i,j in dict1.items():
#     print(i,"roll Number is: ",j)

# for item in dict1:
#     print(item)

# quiz--print the only numeric value>6 in list
list3 = ["rohan", "pokar", 25, 65, 74, 41, 65, 25, 85, 96, 32, 6, 4]
for values in list3:
    if str(values).isnumeric() and values >= 6:
        print(values, end=" ")
