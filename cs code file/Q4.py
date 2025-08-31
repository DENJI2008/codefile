import pickle
with open("student.dat", "wb") as f:
    pickle.dump([{"roll": 101, "name": "Raj"}, {"roll": 102, "name": "Simran"}], f)
roll = int(input("Enter roll number to search: "))

with open("student.dat", "rb") as f:
    students = pickle.load(f)
    for s in students:
        if s["roll"] == roll:
            print("Name:", s["name"])
            break
    else:
        print("Roll No. Not Found")
    
