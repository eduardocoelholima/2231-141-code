a_range = range(1,20,2)
print(a_range)
print(a_range[0])
print(a_range[len(a_range) - 1])

i = 0
while i < len(a_range):
    print(a_range[i], end = ':')
    i += 1
print()

for val in a_range:
    print(val, end=':')
print()