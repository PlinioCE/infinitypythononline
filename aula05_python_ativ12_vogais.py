def vogais(a):
    """
    Função conta o número de vogais contidas na palavra informada pelo usuário
    :param a: palavra informada pelo usuário
    :return: o número de vogais contidas na palavra informada pelo usuário
    """
    v = 'AEIOU'
    vogal = 0
    for i in v:
        vogal += a.count(i)
    return vogal


palavra = str(input('Digite uma palavra: ')).strip().upper()
resultado = vogais(palavra)
print(f'\nA palavra {palavra} tem {resultado} vogais.')
