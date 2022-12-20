def area_retangulo(b, h):
    """
    Função calcula área (cm²) de um retângulo
    :param b: Valor da base do retângulo informado pelo usuário
    :param h: Valor da altura do retângulo informado pelo usuário
    :return: resultado do cálculo da área do retângulo
    """
    a = (b * h)
    return a


base = float(input('Digite o valor da base do triângulo (cm): '))
altura = float(input('Digite o valor da altura do triângulo (cm): '))
resultado = area_retangulo(base, altura)
print(f'\nA área do retângulo corresponde a {resultado} cm².')
