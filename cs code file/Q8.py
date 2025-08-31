import csv
with open("users.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["user1", "pass123"])
    w.writerow(["user2", "abc456"])
uid = input("Enter userid: ")
with open("users.csv", "r") as f:
    r = csv.reader(f)
    for row in r:
        if row[0] == uid:
            print("Password:", row[1])
            break
    else:
        print("User not found")
 
