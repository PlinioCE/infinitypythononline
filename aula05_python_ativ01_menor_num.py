def menor_numero(x, y):
    """
    Função calcula o menor número entre os informados pelo usuário
    :param x: primeiro número informado pelo usuário
    :param y: segundo número informado pelo usuário
    :return: o menor entre os dois números informados pelo usuário
    """
    if x > y:
        menor = f'O menor número é: {y}'
    elif x < y:
        menor = f'O menor número é: {x}'
    else:
        menor = 'Os números são iguais.'
    return menor


numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
resultado = menor_numero(numero1, numero2)
print(f'\n{resultado}')
