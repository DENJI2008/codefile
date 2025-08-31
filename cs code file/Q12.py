nums = [10, 20, 30, 40, 50]
try:
    idx = int(input("Enter index: "))
    print("Element:", nums[idx])
except ValueError:
    print("Enter integers only!")
except IndexError:
    print("Index out of range!")
else:
    print("Element accessed successfully")
