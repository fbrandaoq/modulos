
def exibir_menu():
    print('1 - Calcular quadrilátero')
    print('2 - Calcular círculo')
    print('3 - Calcular triângulo')
    print('4 - Calcular trapézio')
    print('5 - Sair do programa')

# função do quadrilatero
def calcular_quadrilatero(b, h):
    a = b * h
    return a

# função da circunferência
def calcular_circulo(r):
    a = 3.14*r**2
    return a

# função do triangulo
def calcular_triangulo(b, h):
    a = (b * h)/2
    return a

# função do trapezio
def calcular_trapezio(b_menor, b_maior, h):
    a = ((b_menor + b_maior)*h)/2
    return a
