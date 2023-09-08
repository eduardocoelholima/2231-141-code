A_GLOBAL = 5

def function_1():
    x = 1
    print(x)
    print(A_GLOBAL)

def function_2():
    y = 2
    print(y)
    function_1()
    print(A_GLOBAL)

function_2()