int_set = set()
for i in range(0,30,3):
    int_set.add(i)
for ele in int_set:
    print(ele, end = ' ')
print()

string_set = set("Here is the string we are adding to a set")
sorted_list = sorted(string_set)
for ele in sorted_list:
    print(ele, end = ' ')
print()