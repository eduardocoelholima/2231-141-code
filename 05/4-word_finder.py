def does_file_contain_word(filename:str, word:str)->bool:
    with open(filename) as file:
        for line in file:
            stripped = line.strip()
            if stripped == word:
                return True
    return False

def main():
    done = False
    while not(done):
        filename = input('Enter a filename to check: ')
        word = input('Enter a word to look for: ')
        if does_file_contain_word(filename, word):
            print(filename, ' contains ', word)
        else:
            print(filename, ' does NOT contain ', word)
        again = input('Check for another word (y/n)?')
        if again == 'n' or again == 'N':
            done = True
    print('Thanks for checking words!')

if __name__ == '__main__':
    main()