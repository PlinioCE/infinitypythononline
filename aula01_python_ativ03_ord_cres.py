def ordem(x, y, z):
    """
    A função coloca em ordem crescente os números informados pelo usuário
    :param x: primeiro número informado pelo usuário
    :param y: segundo número informado pelo usuário
    :param z: terceiro número informado pelo usuário
    :return: ordem crescente dos números informados pelo usuário
    """
    if x > y and x > z:
        if y > z:
            return z, y, x
        else:
            return y, z, x
    elif y > x and y > z:
        if x > z:
            return z, x, y
        else:
            return x, z, y
    elif z > x and z > y:
        if x > y:
            return y, x, z
        else:
            return x, y, z


numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))
resultado = ordem(numero1, numero2, numero3)
print(f'\nA ordem crescente dos número informados é: {resultado}.')
