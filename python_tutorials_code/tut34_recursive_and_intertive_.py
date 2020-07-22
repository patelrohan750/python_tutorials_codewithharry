def factorial_Iterative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


n = int(input("Enter the Number: "))
print("Iterative method: ", factorial_Iterative(n))
print("recursive method: ", factorial_recursive(n))
