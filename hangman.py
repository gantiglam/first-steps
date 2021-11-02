import random


class Word(object):

    def __init__(self, letters, guessed_letters):

        self.letters = letters
        self.guessed_letters = guessed_letters

    def print_word(self):
        s = ''
        for i in self.letters:
            if i in self.guessed_letters:
                s += i
            else:
                s += '-'
        print(s)


def game(glossary):

    word = Word(list(random.choice(glossary)[0:-1]), guessed_letters={})
    num_of_mist = 0
    num_of_let = len(dict.fromkeys(word.letters))
    print('Guess the hidden word letter by letter')
    word.print_word()
    while num_of_mist < 7 and num_of_let > 0:
        letter = input("Type the letter: ")
        if letter not in word.letters:
            print("There's no such letter in this word")
            print("The gallows is being built!")
            num_of_mist += 1
            draw_gallows(num_of_mist, gallows)
            word.print_word()
            continue
        if letter in word.letters and letter not in word.guessed_letters:
            print("Yes, you've guessed a letter!")
            word.guessed_letters[letter] = 1
            num_of_let -= 1
            word.print_word()
            continue
        if letter in word.letters and letter in word.guessed_letters:
            print("You've already guessed this letter!")
            word.print_word()
            continue
    else:
        if num_of_let == 0:
            print("Congratulations! You won!")
        if num_of_mist == 7:
            print("The man has been hanged, you lost")
            print("The hidden word is ", *word.letters)
    y_or_no = input("Play again? (Y/N): ")
    while y_or_no in {'Y', 'y', 'yes', 'Yes'}:
        game(glossary)
    else:
        exit()


def draw_gallows(n, gallows):  # drawing of gallows
    if n == 1:
        for i in range(5, 7):
            print(gallows[i], end='')
    if n == 2:
        for i in range(2, 7):
            print(gallows[i], end='')
    if n == 3:
        for i in range(0, 7):
            print(gallows[i], end='')
    if n == 4:
        for i in range(7, 9):
            print(gallows[i], end='')
        for i in range(2, 7):
            print(gallows[i], end='')
    if n == 5:
        for i in range(7, 10):
            print(gallows[i], end='')
        for i in range(3, 7):
            print(gallows[i], end='')
    if n == 6:
        for i in range(7, 11):
            print(gallows[i], end='')
        for i in range(4, 7):
            print(gallows[i], end='')
    if n == 7:
        for i in range(7, 12):
            print(gallows[i], end='')
        for i in range(5, 7):
            print(gallows[i], end='')


gallows = open('gallows.txt', 'r').readlines()
glossary = open('dictionary.txt', 'r', encoding='utf8').readlines()

print('H A N G M A N')
ans = input("Type 'play' to play the game or type 'exit' to quit: ")
if ans == 'exit':
    exit()
elif ans == 'play':
    game(glossary)
