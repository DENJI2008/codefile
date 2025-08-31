def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
     n = int(input("Enter any number: "))
     print("The factorial of given number is: ",factorial(n))
main()
