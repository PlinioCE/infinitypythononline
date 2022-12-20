def pares(x, y):
    """
    Função conta os números pares informados pelo usuário
    :param x: primeiro número informado pelo usuário
    :param y: segundo número informado pelo usuário
    :return: a quantidade de números pares
    """
    if x == 0:
        x = 1
    if y == 0:
        y = 1
    if x % 2 == 0 and y % 2 == 0:
        resp = 'Foram digitados 2 números pares.'
    elif x % 2 == 1 and y % 2 == 1:
        resp = 'Não foram digitados números pares.'
    else:
        resp = 'Foi digitado um número par.'
    return resp


numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
resultado = pares(numero1, numero2)
print(f'\n{resultado}')
