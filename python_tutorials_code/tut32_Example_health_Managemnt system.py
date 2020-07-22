# Health management system
# 3 clients -harry,rohan and ,Hammad
import datetime


def getDate():
    return datetime.datetime.now()


# total 6 files
# write a function that when executted takes as input client name
# [] roti sabji
# one more function to retervies exersises or food for any client
def Log(client_choice):
    if client_choice == 1:
        ch = int(input("Press 1 For Food Press 2 for Exercise: "))
        if ch == 1:
            str1 = input("Write here......\n")
            with open("harry_food.txt", "a") as f:
                f.write(str([str(getDate())]) + ":" + str1+"\n")
            print("successfully write.. ")
        elif ch == 2:
            str1 = input("Write here......\n")
            with open("harry_Exercise.txt", "a") as f:
                f.write(str([str(getDate())]) + ":" + str1+"\n")
            print("successfully write.. ")
    elif client_choice == 2:
        ch = int(input("Press 1 For Food Press 2 for Exercise: "))
        if ch == 1:
            str1 = input("Write here......\n")
            with open("rohan_food.txt", "a") as f:
                f.write(str([str(getDate())]) + ":" + str1+"\n")
            print("successfully write.. ")
        elif ch == 2:
            str1 = input("Write here......\n")
            with open("rohan_Exercise.txt", "a") as f:
                f.write(str([str(getDate())]) + ":" + str1+"\n")
            print("successfully write.. ")
    elif client_choice == 3:
        ch = int(input("Press 1 For Food Press 2 for Exercise: "))
        if ch == 1:
            str1 = input("Write here......\n")
            with open("hammad_food.txt", "a") as f:
                f.write(str([str(getDate())]) + ":" + str1+"\n")
            print("successfully write.. ")
        elif ch == 2:
            str1 = input("Write here......\n")
            with open("hammad_Exercise.txt", "a") as f:
                f.write(str([str(getDate())]) + ":" + str1+"\n")
            print("successfully write.. ")
    else:
        print("You Enter Wrong Input!!!!!!!")


def Retrieve(client_choice):
    if client_choice == 1:
        ch = int(input("Press 1 For Food Press 2 for Exercise: "))
        if ch == 1:

            with open("harry_food.txt") as f:
                for i in f:
                    print(i,end="")
        elif ch == 2:

            with open("harry_Exercise.txt") as f:
                for i in f:
                    print(i, end="")

    elif client_choice == 2:
        ch = int(input("Press 1 For Food Press 2 for Exercise: "))
        if ch == 1:

            with open("rohan_food.txt") as f:
                for i in f:
                    print(i, end="")

        elif ch == 2:

            with open("rohan_Exercise.txt") as f:
                for i in f:
                    print(i, end="")

    elif client_choice == 3:
        ch = int(input("Press 1 For Food Press 2 for Exercise: "))
        if ch == 1:

            with open("hammad_food.txt") as f:
                for i in f:
                    print(i, end="")

        elif ch == 2:

            with open("hammad_Exercise.txt") as f:
                for i in f:
                    print(i,end="")

    else:
        print("You Enter Wrong Input!!!!!!!")


print("\t\t\t\t\t Welcome to Health Management System")

x = int(input("Press 1 For Log And Press 2 For Retrieve: "))
# print("Select The Clients ")
if x == 1:
    client_choice = int(input("Press 1 for Harry press 2 for Rohan Press 3 For Hammad: "))
    Log(client_choice)

elif x == 2:
    client_choice = int(input("Press 1 for Harry press 2 for Rohan Press 3 For Hammad: "))
    Retrieve(client_choice)

else:
    print("You Enter Invalid Input")
