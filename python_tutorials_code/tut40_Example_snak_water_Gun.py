# Snake,Water,Gun
# 10times
import random

game_list = ["Snake", "Water", "Gun"]
n = 0
cpu = 0
user = 0
print("\n\t\t\t\t\t\t\t\t\t\t\t Snake-Water-Gun Game\n")
while n < 10:
    user_choice = input("Press S For Snake,W for water,G for Gun: ")
    cpu_choice = random.choice(game_list)
    if user_choice.upper() == "S":

        if cpu_choice == "Snake":
            print(user_choice, "=", cpu_choice)
            print("Tie")

        elif cpu_choice == "Water":
            print(user_choice, "=", cpu_choice)
            print("user won")
            user += 1

        elif cpu_choice == "Gun":
            print(user_choice, "=", cpu_choice)
            print("cpu won")
            cpu += 1
    elif user_choice.upper() == "W":

        if cpu_choice == "Snake":
            print(user_choice, "=", cpu_choice)
            print("cpu won")
            cpu += 1
        elif cpu_choice == "Water":
            print(user_choice, "=", cpu_choice)
            print("Tie")
        elif cpu_choice == "Gun":
            print(user_choice, "=", cpu_choice)
            print("user won")
            user += 1
    elif user_choice.upper() == "G":

        if cpu_choice == "Snake":
            print(user_choice, "=", cpu_choice)
            print("user won")
            user += 1
        elif cpu_choice == "Water":
            print(user_choice, "=", cpu_choice)
            print("cpu won")
            cpu += 1
        elif cpu_choice == "Gun":
            print(user_choice, "=", cpu_choice)
            print("Tie")
    else:
        print("Invalid Input!!!!!")
    n = n + 1
    print("Remaining chance is: ", 10 - n)

print("cpu score is: ", cpu)
print("user score is: ", user)
if user > cpu:
    print("User Is Winner!!!!!!!")
elif user < cpu:
    print("Cpu Is Winner!!!!!!!")
else:
    print("Match Tie")
