with open("sample.txt", "r") as f:
    for line in f:
        words = line.strip().split()
        print("#".join(words))
