import main_guard

def function_2():
    print('Function 2')

def main():
    print('Import Complete')
    function_2()
    main_guard.function_1()

main()
