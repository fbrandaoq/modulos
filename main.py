# faz as importações
import os
from modulo import *

# programa principal
if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')

        match opcao:
            case '1':
                # entrada de dados
                b = int(input('Base do quadriláterio: '))
                h = int(input('Altura do quadrilátero: '))
                print(f'Área: {calcular_quadrilatero(b, h)}')
                continue
            case '2':
                r = int(input('Raio do círculo: '))
                print(f'Área: {calcular_circulo(r)}')
                continue
            case '3':
                b = int(input('Base do triângulo: '))
                h = int(input('Altura do triângulo: '))
                print(f'Área: {calcular_triangulo(b, h)}')
                continue
            case '4':
                b_menor = int(input('Base menor do trapezio: '))
                b_maior = int(input('Base maior do trapezio: '))
                h = int(input('Altura do trapezio: '))
                print(f'Área: {calcular_trapezio(b_menor, b_maior, h)}')
                continue
            case '5':
                break

