def menor_limite(a, b, limite):
    """
    Função verifica se a soma dos número é maior ou menor que o limite informado pelo usuário
    :param a: primeiro número informado pelo usuário
    :param b: segundo número informado pelo usuário
    :param limite: limite informado pelo usuário
    :return: True caso a soma dos números seja maior que o limite e False caso essa soma seja menor.
    """
    if (a + b) > limite:
        resp = True
    else:
        resp = False
    return resp


numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
limite = int(input('Informe o limite: '))
resultado = menor_limite(numero1, numero2, limite)
print()
print(resultado)
