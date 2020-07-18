# d1={}
# print(type(d1))
d2={11:"pokr",12:"rohan",13:"rahul","Rohan":{"S":"coding","sa":"python","N":"gaming"},"list1":[11,12,13,14,15,1,6]}
print(d2)

print(d2["Rohan"])
print(d2["Rohan"]["S"])
d2["test"]=150
print(d2)
d2[11]="pokar"
print(d2)
# d3=d2.copy()
# print(d3)
# d3.pop(12)
# print(d3)
print(d2.items())
print(d2.values())