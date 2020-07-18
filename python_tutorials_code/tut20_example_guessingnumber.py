# guessing the number
# no of guesses 9
# print no of guesses left
# no of guesses he took the finish
# game over
n = 18
guesses = 0
print("welcome to the Guessesing Number game!!!!!!!!\n")
print("you have total 9 chance to find out guessesing numbere.......\n")
while guesses < 9:
    num = int(input("Enter Number: "))
    if num == n:
        print("You won...")
        print("you take ", guesses, " chance to finish ")
        break
    elif num > n:
        print("you value is highre then guesses value...\n")
    elif num < n:
        print("you value is less then guesses value...\n")
    guesses += 1
    print("your remaining chance is: ", 9 - guesses)
    if guesses == 9:
        print("game is over!!!!!!!!!!")
