
with open('filename.txt') as fh:
    for line in fh:
        line = line.rstrip()
        print(line)

print("Done")

fh = open('filename.txt')
for line in fh:
    print(line)

fh.close()
