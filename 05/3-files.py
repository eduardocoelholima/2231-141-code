f = open('words2.txt')
for line in f:
    stripped = line.strip()
    print(stripped)
f.close()

with open('words2.txt') as f:
    for line in f:
        stripped = line.strip()
        print(stripped)

