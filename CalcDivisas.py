# -*- coding:utf-8 -*-

def calcular_divisa(cantidad):
    mex_to_col = 145.97
    return mex_to_col * cantidad

def main():
    print('CALCULADORA DE DIVISAS')
    print('Convierte de pesos mexicanos a pesos colombianos.')
    print('')
    cantidad = float(input('Ingresa la cantidad de pesos mexicanos que deseas convertir: '))
    resultado = calcular_divisa(cantidad)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(cantidad, resultado))
    print('')


if __name__ == '__main__':
    main()
