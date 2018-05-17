# -*- coding:utf-8 -*-

def palindromo(palabra):
    letrasrev = []

    for letter in palabra:
        letrasrev.insert(0, letter)

    palabrarev = ''.join(letrasrev)

    if palabrarev == palabra:
        return True
    else:
        return False

def palindromo2(palabra):
    palabrarev = palabra[::-1]

    if palabrarev == palabra:
        return True
    else:
        return False


if __name__ == '__main__':
    palabra = str(input('Escribe una palabra: '))
    resultado = palindromo2(palabra)

    if resultado is True:
        print('La palabra {} es un palíndromo'.format(palabra))
    else:
        print('La palabra {} NO es un palíndromo'.format(palabra))
