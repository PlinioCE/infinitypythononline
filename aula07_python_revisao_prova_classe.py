# classificacao_dicionario.py

def ordenar_dicionario(dicionario):
    print('*** CLASSIFICAÇÃO GERAL ***')
    print('******* WSL - 2023 ********')
    print('***************************')
    colocacao = 1
    for item in sorted(dicionario, key=dicionario.get, reverse=True):
        print(f'{colocacao}º - {item:<10} {dicionario[item]:>11}')
        colocacao += 1
