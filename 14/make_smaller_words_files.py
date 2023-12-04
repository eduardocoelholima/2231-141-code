import random
MIN_WORD_SIZE = 11
MAX_WORDS = 30000
words = []
with open('data/words_alpha.txt') as file:
    for line in file:
        stripped = line.strip()
        if len(stripped) > MIN_WORD_SIZE:
            words.append((stripped))
print(len(words))
random.shuffle(words)
words = words[:MAX_WORDS]
with open('data/words_long.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')
