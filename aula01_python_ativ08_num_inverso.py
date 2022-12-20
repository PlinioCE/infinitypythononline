def num_invertido(x):
    """
    Função recebe número informado pelo usuário e inverte a ordem dos algarismos
    :param x: número informado pelo usuário
    :return: número invertido ao informado pelo usuário
    """
    texto = str(x)
    inverso = texto[::-1]
    num = int(inverso)
    return num


numero = int(input('Digite um número: '))
resultado = num_invertido(numero)
print(f'\nO número {numero} invertivo fica, {resultado}.')
