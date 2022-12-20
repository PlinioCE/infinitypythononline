def fatorial(x, show=False):
    """
    Função calcula fatorial do número informado pelo usuário, exibindo ou não o cálculo
    :param x: número informado pelo usuário a ser calculado o fatorial
    :param show: parâmetro lógico para exibição do cálculo. True = exibir, False = não exibir
    :return: o resultado do cálculo fatorial
    """
    f = 1
    print(f'\n{x}! = ', end='')
    for n in range(x, 0, -1):
        f *= n
        if show:
            if n == 1:
                print(f'{n} = ', end='')
            else:
                print(f'{n} x ', end='')
    return f


numero = int(input('Digite um número: '))
calc = str(input('Deseja exibir o cálculo? [S/N]: ')).strip().upper()[0]
while calc not in 'SN':
    calc = str(input('Deseja exibir o cálculo? [S/N]: ')).strip().upper()[0]
if calc == 'S':
    calc = True
else:
    calc = False
resultado = fatorial(numero, calc)
print(resultado)
