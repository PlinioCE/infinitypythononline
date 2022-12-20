def craps():
    """
    Função sorteia dois números(dados) para o jogo CRAPS.
    O jogador lança um par de dados, obtendo um valor entre 2 e 12.
    Se, na primeira jogada, você tirar 7 ou 11, você é um "natural"
    e venceu o jogo. Se você tirar 2, 3 ou 12 na primeira jogada,
    isto é chamado de "craps" e você perdeu. Se, na primeira jogada,
    você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo
    agora é continuar jogando os dados até tirar este número novamente.
    Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
    :return: sem retorno
    """
    from random import randint
    from time import sleep
    contador = 1
    while True:
        print(f'--- {contador}ª JOGADA ---')
        sleep(1)
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        print('MEXENDO OS DADOS')
        sleep(1.5)
        print(f'1º DADO: {dado1}')
        sleep(1)
        print(f'2º DADO: {dado2}')
        sleep(1)
        soma = dado1 + dado2
        if contador == 1 and soma == 7 or contador == 1 and soma == 11:
            print(f'\n{soma}! PARABÉNS, VOCÊ VENCEU E É UM NATURAL!')
            break
        elif contador == 1 and soma == 2 or contador == 1 and soma == 3 or contador == 1 and soma == 12:
            print(f'\n{soma}! CRAPS!!! VOCÊ PERDEU!')
            break
        elif contador == 1:
            ponto = soma
            print(f'VOCÊ FEZ {ponto} pontos.')
        if contador > 1 and soma == ponto:
            print(f'\n{soma}! PARABÉNS, VOCÊ VENCEU!')
            break
        elif contador > 1 and soma == 7:
            print(f'\n{soma}! CRAPS!!! VOCÊ PERDEU!')
            break
        contador += 1


partida = str(input('Deseja jogar uma partida de CRAPS? [S/N]: ')).strip().upper()[0]
if partida == 'S':
    craps()
else:
    print('\n***** FINALIZANDO JOGO *****')
