def soma_global(x):
    """
    Função soma número informado pelo usuário e uma variável global
    :param x: número informado pelo usuário
    :return: a soma entre o número informado pelo usuário e a variável global
    """
    global y
    resp = x + y
    return resp


y = 1
numero = int(input('Digite um número: '))
resultado = soma_global(numero)
print(f'\nA soma entre o número {numero} e a variável global = {resultado}')
