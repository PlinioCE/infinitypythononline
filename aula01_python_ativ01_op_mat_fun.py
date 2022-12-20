def operadores(x, y):
    """
    Função realiza as 4 operações aritiméticas básicas (+, -, *, /)
    :param x: primeiro número fornecido pelo usuário
    :param y: segundo número fornecido pelo usuário
    :return: soma, subtração, produto e divisão
    """
    soma = x + y
    subtracao = x - y
    multiplicacao = x * y
    divisao = x / y
    return soma, subtracao, multiplicacao, divisao


numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
som, sub, mult, div = operadores(numero1, numero2)
print(f'\n{numero1} + {numero2} = {som}'
      f'\n{numero1} - {numero2} = {sub}'
      f'\n{numero1} x {numero2} = {mult}'
      f'\n{numero1} : {numero2} = {div}')
