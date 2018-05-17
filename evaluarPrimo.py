# -*- coding:utf-8 -*-

def run():
    number = int(input('Escribe un número: '))
    resultado = esPrimo(number)
    if resultado == True:
        print('Es primo')
    else:
        print('NO es primo')


def esPrimo(number):
    contador = 0

    for i in range(1, number + 1):
        if number % i == 0:
            contador = contador + 1

    if contador == 2:
        return True
    else:
        return False

if __name__ == '__main__':
    run()
