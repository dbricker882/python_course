filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for n in filenames:
    file = open(n, "w")
    file.write("Hello")
    file.close