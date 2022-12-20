def menor_limite(a, b, limite):
    """
    Função verifica quantos números são maiores ou menores que o limite informado pelo usuário
    :param a: primeiro número informado pelo usuário
    :param b: segundo número informado pelo usuário
    :param limite: limite informado pelo usuário
    :return: a quantidade de números maiores que o limite.
    """
    if a > limite and b > limite:
        resp = 2
    elif a < limite and b < limite:
        resp = 0
    else:
        resp = 1
    return resp


numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
limite = int(input('Informe o limite: '))
resultado = menor_limite(numero1, numero2, limite)
print()
print(f'Foram inserido {resultado} número(s) maior(es) que o limite.')
