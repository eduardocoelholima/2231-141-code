sample_string = 'This is a string'
print(sample_string[0])
print(sample_string[len(sample_string) - 1])

i = 0
while i < len(sample_string):
    print(sample_string[i], end=':')
    i += 1
print()

string_1 = 'Hello'
string_2 = 'World'
string_3 = string_1 + string_2 + str(123)
print(string_3)

for letter in sample_string:
    print(letter, end=':')
print()

for letter in sample_string:
    print(letter, '-',ord(letter))

for val in range(65,91):
    print(chr(val), end = '')
print()

print(sample_string[:])
print(id(sample_string), id(sample_string[:]))
print(sample_string[::-1])
print(id(sample_string), id(sample_string[::-1]))
