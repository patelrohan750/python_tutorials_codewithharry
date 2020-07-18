# brek and continue
# i = 0
# while True:
#     if i < 5:
#         i = i + 1
#         continue
#     print(i, end=" ")
#     if i == 35:
#         break
#
#     i = i + 1

# quiz--take input from user and Enter te value again and again when user enter value is >100
# then print the startment anything

while True:
    num = int(input("Enter Number:\n"))
    if num>100:
        print("congratulations you enter the greaterthen value of 100\n")
        break
    else:
        print("try again....")
        continue
