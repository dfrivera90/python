# -*- coding: utf-8 -*-
from lamp import Lampara

def run():
    lamp = Lampara(is_turned_on=False)

    while True:
        comando = str(input('''
            Qué deseas hacer?

            [p]Prender
            [a]Apagar
            [s]Salir
        '''))
        if comando == 'p':
            lamp.turn_on()
        elif comando == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()
