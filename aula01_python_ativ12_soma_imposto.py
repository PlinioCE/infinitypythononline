def soma_imposto():
    """
    Função calcula imposto sobre item que altera o preço
    :return: sem retorno
    """
    custo = float(input('Digite o custo do item: R$ '))
    taxa_imposto = float(input('Digite a porcentagem do imposto: '))
    novo_custo = custo + (custo * taxa_imposto / 100)
    print(f'\nCUSTO + IMPOSTO: R$ {novo_custo:.2f}')


saida = ' '
while saida not in 'SN':
    saida = str(input('Deseja calcular o imposto sobre item? [S/N]: ')).strip().upper()[0]
if saida == 'S':
    soma_imposto()
else:
    print('\n***** FINALIZANDO SISTEMA *****')
