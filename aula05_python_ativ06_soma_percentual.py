def percentual(x, y):
    """
    Função calcula a porcentagem do valor informado pelo usuário
    :param x: valor fornecido pelo usuário
    :param y: valor da porcentagem fornecido pelo usuário
    :return: o valor mais a porcentagem
    """
    resp = x + (x * y / 100)
    return resp


numero = float(input('Informe o valor: R$ '))
porcentagem = float(input('Informe a porcentagem que deseja calcular: '))
resultado = percentual(numero, porcentagem)
print(f'\nR$ {resultado:.2f}')
