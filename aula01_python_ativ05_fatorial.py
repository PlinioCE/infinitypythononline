def fatorial(x):
    """
    Função calcula fatorial do número informado pelo usuário
    :param x: número informado pelo usuário
    :return: o fatorial do número informado pelo usuário
    """
    fat = 1
    for n in range(x, 0, -1):
        fat *= n
    return fat


numero = int(input('Digite um número: '))
resultado = fatorial(numero)
print(f'\n{numero}! = {resultado}')
