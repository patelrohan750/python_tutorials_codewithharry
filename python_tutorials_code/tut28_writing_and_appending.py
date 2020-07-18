# f=open("tut28_test.txt","w")
# f.write("hello friends how are you!!!!!!!!")
# f.close()

# f=open("tut28_test.txt","a")
# f.write("hello friends how are you\n")
# f.close()

# read and write both using

f=open("tut28_test.txt","r+")
print(f.read())
f.write("hello friends\n")
f.write("love coding\n")
f.write("learn python\n")

f.close()