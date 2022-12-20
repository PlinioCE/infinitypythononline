def par():
    """
    Função verifica qual maior número par
    :return: maior número par
    """
    par1 = par2 = 1
    while par1 % 2 == 1 or par1 == 0:
        par1 = int(input('Informe o 1º número par: '))
    while par2 % 2 == 1 or par2 == 0:
        par2 = int(input('Informe o 2º número par: '))
    if par1 > par2:
        maior_par = par1
    elif par1 < par2:
        maior_par = par2
    else:
        maior_par = par1
    return maior_par


def impar():
    """
    Função verifica o maior número ímpar
    :return: o maior número ímpar
    """
    impar1 = impar2 = 2
    while impar1 % 2 == 0 or impar1 == 0:
        impar1 = int(input('Informe o 1º número ímpar: '))
    while impar2 % 2 == 0 or impar2 == 0:
        impar2 = int(input('Informe o 2º número ímpar: '))
    if impar1 > impar2:
        maior_impar = impar1
    elif impar1 < impar2:
        maior_impar = impar2
    else:
        maior_impar = impar1
    return maior_impar


resultado_par = par()
resultado_impar= impar()
print(f'\nA soma do maior PAR e do maior ÍMPAR = {resultado_par + resultado_impar}.')
