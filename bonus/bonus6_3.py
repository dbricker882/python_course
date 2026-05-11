filenames = ["a.txt", "b.txt", "c.txt"]

for n in filenames:
    file = open(n, "r")
    contents = file.read()
    print(contents)
    
