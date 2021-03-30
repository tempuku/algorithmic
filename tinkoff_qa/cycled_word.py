import sys
from itertools import cycle


def check_cycled(symbols, word):
    cycled_symbols = cycle(symbols)
    word_copy = word
    cycled_symbols.__next__()
    for sym in cycled_symbols:
        if not word_copy:
            return 'YES'
        if word_copy[0] == sym:
            word_copy = word_copy[1:]
        else:
            return 'NO'


def check_other_symbols(symbols, word, i):
    right_answer = check_cycled(symbols[i:] + symbols[:i], word)
    left_answer = check_cycled(symbols[i::-1] + symbols[:i:-1], word)
    if right_answer == 'YES' or left_answer == 'YES':
        return 'YES'
    else:
        return 'NO'


def cycled_word(symbols: str, word: str):
    for i in range(len(symbols)):
        if symbols[i] == word[0]:
            answer = check_other_symbols(symbols, word[1:], i)
            if answer == 'YES':
                return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    stdin = sys.stdin
    symbols = stdin.readline().rstrip()
    word = stdin.readline().rstrip()
    print(cycled_word(symbols, word))
