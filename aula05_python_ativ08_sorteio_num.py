def sorteio(x, y):
    """
    Função sorteia um número no intervalo definido pelo usuário
    :param x: valor para inicio do intervalo definido pelo usuário
    :param y: valor para fim do intervalo definido pelo usuário
    :return: número sorteado
    """
    from random import randrange
    resp = randrange(x, y)
    return resp


inicio = int(input('Digite o número de início: '))
fim = int(input('Digite o número de fim: '))
resultado = sorteio(inicio, fim)
print(f'\nO número sorteado foi: {resultado}')
