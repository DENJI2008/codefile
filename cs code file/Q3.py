f = open("sample.txt", "r")
out = open("output.txt", "w")
for line in f:
    if 'a' not in line:
        out.write(line)
f.close()
out.close()
        
