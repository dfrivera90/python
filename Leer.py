# -*- coding: utf-8 -*-

def run():
    contador = 0;
    with open('Aleph.txt') as fuck:
#        Comando para leer un archivo y convertirlo en lista
#        print(fuck.readlines())
        for line in fuck:
            contador += line.count('Beatriz')
    print ('Beatriz se encuentra {} en el texto'.format(contador))

if __name__ == '__main__':
    run()
