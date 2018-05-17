# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado',
    'zorra',
    'pendeja',
    'chupelo'
]

def randon_word():
    index = random.randint(0, len(WORDS)-1)
    return WORDS[index]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---')


def run():
    word = randon_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Digita una letra: '))

        letter_indxs = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indxs.append(i)

        if len(letter_indxs) == 0:
            tries +=1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Maldito Animal, perdiste. La palabra correcta era {}'.format(word))
                break
        else:
            for i in letter_indxs:
                hidden_word[i] = current_letter

            letter_indxs = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Ganaste Carechimba!')
            break


if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S : E L  J U E G O')
    run()
