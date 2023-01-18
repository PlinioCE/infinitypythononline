def contar_letras(texto):
    """
    Função realiza a contagem de letras contidas no parâmentro.
    :param texto: String fornecida pelo usuário.
    :return: A quantidade de letras contidas no parâmetro.
    """
    if ' ' not in texto:
        texto = texto.lower()
        quantidade_letras = len(texto)
    elif ' ' in texto:
        texto = texto.replace(' ', '')
        quantidade_letras = len(texto)
    return quantidade_letras


palavra = str(input('Digite uma palavra ou frase: '))
print()
print(f'A palavra/frase {palavra.upper()}, contém {contar_letras(palavra)} letras.')
