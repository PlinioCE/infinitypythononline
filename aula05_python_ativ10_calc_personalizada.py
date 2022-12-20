def calc(x, y, z):
    """
    Função calcula operação de acordo com definição do usuário
    :param x: primeiro número informado pelo usuário
    :param y: segundo valor informado pelo usuário
    :param z: operador informado pelo usuário
    :return: resultado do cálculo
    """
    if z == '+':
        resp = f'{x} + {y} = {x + y}'
    elif z == '-':
        resp = f'{x} - {y} = {x - y}'
    elif z == '*' or z == 'x':
        resp = f'{x} x {y} = {x * y}'
    elif z == '/' or z == ':':
        resp = f'{x} : {y} = {x / y}'
    else:
        resp = 'OPERADOR INVÁLIDO!'
    return resp


numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
operador = str(input('Informe o operador (+, -, x, /): '))
resultado = calc(numero1, numero2, operador)
print(f'\n{resultado}')
