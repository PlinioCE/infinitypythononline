def somatorio(a):
    """
    Função calcula soma dos números de 0 (zero) ao número informado
    :param a: número informado pelo usuário
    :return: somatório dos números entre 0 (zero) e "a" (número informado pelo usuário)
    """
    contador = 0
    for i in range(0, a+1):
        contador += i
    return contador


numero = int(input('Digite um número: '))
resultado = somatorio(numero)
print(f'\nO somatório dos números entre 0 e {numero} = {resultado}.')
