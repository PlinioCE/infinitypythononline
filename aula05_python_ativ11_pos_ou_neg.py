def sinal(x):
    """
    Função calcula se o número informado pelo usuário é positivo, negativo ou nulo
    :param x: número informado pelo usuário
    :return: se o número informado pelo usuário é positivo, negativo ou nulo
    """
    if x > 0:
        resp = 'POSITIVO'
    elif x < 0:
        resp = 'NEGATIVO'
    else:
        resp = 'NULO'
    return resp


numero = int(input('Digite um número: '))
resultado = sinal(numero)
print(f'\nO número {numero} é {resultado}.')
