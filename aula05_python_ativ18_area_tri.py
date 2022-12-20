def area_triangulo(b, h):
    """
    Função calcula área (cm²) de um triângulo
    :param b: Valor da base do triângulo informado pelo usuário
    :param h: Valor da altura do triângulo informado pelo usuário
    :return: Cálculo da área do triângulo
    """
    a = (b * h) / 2
    return a


while True:
    base = float(input('Digite o valor da base do triângulo (cm): '))
    altura = float(input('Digite o valor da altura do triângulo (cm): '))
    resultado = area_triangulo(base, altura)
    print(f'\nA área do triângulo corresponde a {resultado} cm².')
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja realizar outro cálculo? [S/N]:')).strip().upper()[0]
        print()
    if saida == 'N':
        print('***** FINALIZANDO CALCULADORA *****')
        break
