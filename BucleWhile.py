# -*- coding:utf-8 -*-
import random


def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('Ganaste!!')
            number_found = True
        elif number > random_number:
            print('Intenta un número menor')
        else:
            print('Intenta un numero mayor')

if __name__ == '__main__':
    run()
