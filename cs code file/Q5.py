import pickle
with open("marks.dat", "wb") as f:
    pickle.dump([{"roll": 1, "name": "Aman", "marks": 85},
                 {"roll": 2, "name": "Pooja", "marks": 90}], f)
roll = int(input("Enter roll number to update: "))
with open("marks.dat", "rb") as f:
    students = pickle.load(f)
for s in students:
    if s["roll"] == roll:
        s["marks"] = int(input("Enter new marks: "))
with open("marks.dat", "wb") as f:
    pickle.dump(students, f)

