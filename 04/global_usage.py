A_CONSTANT = 4
A_VARIABLE = 3

def incorrect_add(val:int) -> None:
    global A_VARIABLE
    A_VARIABLE += val
    return

def correct_add(val:int) -> int:
    result = A_CONSTANT + val
    return result

def main():
    # Incorrect usage of globals
    incorrect_add(3)
    print(A_VARIABLE)

    #correct usage of globals
    answer = correct_add(3)
    print(answer)

if __name__ == '__main__':
    main()
