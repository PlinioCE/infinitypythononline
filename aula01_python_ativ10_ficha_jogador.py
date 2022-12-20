def ficha(j='', g=''):
    """
    -> Função informa quantos gols um determinado jogador fez
    :param j: Nome do jogador
    :param g: Número de gols do jogador
    :return: sem retorno
    """
    if j == '':
        j = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = '0'
    resp = f'O jogador {j} marcou {g} gols.'
    return resp


jogador = str(input('Informe o nome do jogador: ')).strip().title()
gols = str(input(f'Informe o número do gol(s) do {jogador}: '))
resultado = ficha(jogador, gols)
print(f'\n{resultado}')
