def add(param_1:int, param_2:int) -> int:
    result = param_1 + param_2
    return result


def main():
    arg_1 = int(input('Enter a number: '))
    arg_2 = int(input('Enter another number: '))
    arg_1_plus_arg_2 = add(arg_1, arg_2)
    print(arg_1_plus_arg_2)


main()
# print(main())
# print(type(main()))
