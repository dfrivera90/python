# -*- coding: utf-8 -*-

def busqueda_binaria(numeros, numero, bajo, alto):

    if bajo > alto:
        return False

    mid = (bajo + alto)//2

    if numeros[mid] == numero:
        return True
    elif numeros[mid]>numero:
        return busqueda_binaria(numeros, numero, bajo, mid-1)
    else:
        return busqueda_binaria(numeros, numero, mid + 1, alto)



if __name__ == '__main__':
    numeros = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    numero = int(input('Ingresa un número: '))

    resultado = busqueda_binaria (numeros, numero, 0, len(numeros) - 1)

    if resultado is True:
        print('El número si está')
    else:
        print('El número NO está')
