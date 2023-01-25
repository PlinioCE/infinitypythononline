# classificacao_dicionario_main.py

from aula07_python_revisao_prova_classe import ordenar_dicionario

# competidor = {'Lucas': 1454, 'Pedro': 1243, 'Ricardo': 1452}
competidor = {}
print('***************************')
print('******* WSL - 2023 ********')
print('***************************')
while True:
    nome = str(input('Nome do competidor: ')).title()
    pontuacao = int(input('Pontuação do competidor: '))
    competidor[nome] = pontuacao
    saida = str(input('Deseja informar outro competidor? [S/N]: ')).upper()
    if saida[0] == 'N':
        break
    print()
print()
ordenar_dicionario(competidor)
