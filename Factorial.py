def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)    #Factorial of an integer using recursion.

integer = int(input("Enter the integer to know the factorial of it : "))
result = factorial(integer)
print("Factorial of {} = {}".format(integer, result))