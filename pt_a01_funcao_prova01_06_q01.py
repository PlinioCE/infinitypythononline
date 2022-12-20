def seculo(x):
    """
    Função exibe o século, em algarismo romano, a partir do ano informado pelo usuário
    :param x: Corresponde ao ano informado pelo usuário;
    :return: O século do ano informado pelo usuário.
    """
    if x == 0:
        sec = 1
    elif x % 100 > 0:
        sec = (x // 100) + 1
    else:
        sec = x // 100
    unidade = sec % 10
    dezena = (sec - unidade)
    if dezena > 0:
        if dezena == 10:
            d_sec = 'X'
        elif dezena == 20:
            d_sec = 'XX'
        elif dezena == 30:
            d_sec = 'XXX'
        elif dezena == 40:
            d_sec = 'XL'
        elif dezena == 50:
            d_sec = 'L'
        elif dezena == 60:
            d_sec = 'LX'
        elif dezena == 70:
            d_sec = 'LXX'
        elif dezena == 80:
            d_sec = 'LXXX'
        elif dezena == 90:
            d_sec = 'XC'
        elif dezena == 100:
            d_sec = 'C'
    else:
        d_sec = ''
    if unidade > 0:
        if unidade == 1:
            u_sec = 'I'
        elif unidade == 2:
            u_sec = 'II'
        elif unidade == 3:
            u_sec = 'III'
        elif unidade == 4:
            u_sec = 'IV'
        elif unidade == 5:
            u_sec = 'V'
        elif unidade == 6:
            u_sec = 'VI'
        elif unidade == 7:
            u_sec = 'VII'
        elif unidade == 8:
            u_sec = 'VIII'
        elif unidade == 9:
            u_sec = 'IX'
    else:
        u_sec = ''
    sec_rom = d_sec + u_sec
    return sec_rom


ano = int(input('Digite um ano: '))
resultado = seculo(ano)
print(f'\nO ano informado corresponde ao Século {resultado}.')
