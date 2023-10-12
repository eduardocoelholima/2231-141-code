# create a string
a_string = "Strings are sequences"
print(type(a_string))
# iterate through the string as a sequence and print all characters on the same line separated by :
for char in a_string:
    print(char, end = ':')
print()
# create a list from the string and print it
a_list = list(a_string)
print(type(a_list))
print(a_list)
# slicing works with lists
print(a_list[8:11])
# unlike strings, lists are mutable
for i in range(8,11):
    a_list[i] = 'X'
print(a_list)
print(a_list[8:11])
# demo using in
range_list = list(range(1, 10, 2))
print(range_list)
for i in range(1, 10):
    print(i, i in range_list)
# add some more stuff to the list using extending
a_list += list('More Stuff')
print(a_list)
# when adding lists they must all be lists
b_list = a_list + ['a']
print(b_list)
# pop the last value off the end of the list and insert it at the front
pop_val = a_list.pop()
a_list.insert(0, pop_val)
print(a_list)

# tokenizing using split
a_string = 'Here is a string, which we can tokenize, using various delimiters'
split_by_space = a_string.split()
print(split_by_space)
split_by_comma = a_string.split(',')
print(split_by_comma)

# create a tuple from the first three elements of the list
a_tuple = tuple(a_list[:3])
print(type(a_tuple), a_tuple)
# tuples are immutable so doing the following would cause an error
# a_tuple[0] = 'F'




