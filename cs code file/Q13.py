def fibonacci(n):
     if n == 0:
       return 0
     elif n == 1:
       return 1
     else:
       return(fibonacci(n-2) + fibonacci(n-1))

nterms = int(input("Please enter the Range Number: "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibonacci(i),end='   ')
