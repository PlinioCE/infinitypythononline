def fizz_buzz(x):
    """
    Função verifica se o número informado pelo usuário é divisível por 3 e 5.
    :param x: número informado pelo usuário
    :return: Fizz caso seja divisível por 3, Buzz caso seja por 5 e FizzBuzz caso seja por 3 e 5.
    """
    if x % 3 == 0 and x % 5 == 0:
        resp = 'FizzBuzz'
    elif x % 3 == 0:
        resp = 'Fizz'
    elif x % 5 == 0:
        resp = 'Buzz'
    else:
        resp = x
    return resp


numero = int(input('Digite um número: '))
resultado = fizz_buzz(numero)
print(f'\nO número {numero} é {resultado}.')
