try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a/b)
except ValueError:
    print("Enter integers only!")
except ZeroDivisionError:
    print("Division by zero not allowed!")
else:
    print("Division successful")
finally:
    print("Program execution completed")
