# prof_name = input("Please type you full name:")
# print("Alright, you told me the professor name is ",
#       prof_name, "but I dont believe you.")

# print("first \"line\"")





#
# age = int(input("Tell your age:"))
# age = age - 10
# print("Oh my, your age is ",age,"????", "yolo", sep="\n")








# def triangle_type(a, b, c):
#     if a == b and b == c:
#         return "equilateral"
#     else:
#         return "no idea"
def triangle_type(a, b, c):
    if a == b and b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

print(triangle_type(1,1,1))

