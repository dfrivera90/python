# -*- coding:utf-8 -*-

def promedio(temps):
    sumatoria = 0

    for temp in temps:
        sumatoria += temp

    return sumatoria / len(temps)


if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]
    resultado = promedio(temps)
    print('La temperatura promedio es: {}'.format(resultado))
