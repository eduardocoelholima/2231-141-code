with open('alice.txt') as file:
    for line in file:
        stripped = line.strip()
        tokens = stripped.split()
        print(tokens)