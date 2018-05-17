# -*- coding: utf-8 -*-
def primer_char_sin_repetir(secuencia):
    seen_letter = {}

    for idx, letra in enumerate(secuencia):
        if letra not in seen_letter:
            seen_letter[letra] = (idx, 1)
        else:
            seen_letter[letra] = (seen_letter[letra][0], seen_letter[letra][1]+1)

    letras_finales = []
    for key, value in seen_letter.items():
        if value[1] == 1:
            letras_finales.append((key, value[0]))


    letras_no_rep = sorted(letras_finales, key = lambda value: value[1])

    if letras_no_rep:
        return letras_no_rep[0][0]
    else:
        return '_'

if __name__ == '__main__':
    secuencia = str(input('Escribe una secuencia de caracteres: '))

    resultado = primer_char_sin_repetir(secuencia)

    if resultado == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter que no se repite es: {}'.format(resultado))
