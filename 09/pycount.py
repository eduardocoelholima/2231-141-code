"""
CSAPX Week 4: Hashing

A word counting program that uses a built in Python dictionary.

author: Sean Strout @ RIT CS
"""

import sys   # argv

def read_words(filename: str) -> dict:
    """
    Read the words from a file into a dictionary that counts the number of
    occurrences of each word.
    :param filename: the file to read
    :return: a dictionary whose keys are words and values are counts
    """
    words = dict()
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word = word.strip(",.\"\';:-!?").lower()
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
    return words

def main() -> None:
    """
    Count the words in a file and display some statistics.
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pycount.py filename')
    else:
        words = read_words(sys.argv[1])
        print(words)
        print("Total words:", sum(words.values()))
        print("Unique words:", len(words))
        most = list(words.values())
        most.sort()
        for word in words:
            if words[word] == most[-1]:
                print('Most used word,', '"' + word + '"' + ' occurred', words[word], 'times.')
    
if __name__ == '__main__':
    main()

