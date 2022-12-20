# [PT-A03] com intuito de organizar o pasto, o fazendeiro que andava estudando
# a linguagem Python queria fazer um arranjo em sua fazenda  usando o método de
# listas, sabendo disso ajude o agrônomo a realizar essa mudança. Levando em
# consideração que no pasto 1 (que também é uma lista)tem  4 listas com um animal
# diferente em cada(animais da sua escolha)e dentro dessas listas havia 4 cores de
# animais(cores da sua escolha porém sempre diferentes),faça um código responsável
# por mudar 3 listas de animais do pasto 1 para o pasto 2 que estava vazio e
# imprimindo o resultado final dos animais do pasto 2 e os animais do pasto 1.
#
# Exemplo de lista de animal:zebras=['zebras=',"branca","bege","preta"],
# OBS: Use as funções de manipulação de listas

pasto_1 = [['vacas = ', 'branca', 'preta', 'malhada', 'marrom'],
           ['ovelhas = ', 'amarela', 'vermelha', 'beje', 'castanho'],
           ['búfalos = ', 'negros', 'cinza escuro', 'marrom escuro', 'albino'],
           ['cavalos = ', 'baio escuro', 'baio amarilho', 'baio encerado', 'rosilho']]
pasto_2 = []

print('### PASTOS ANTES DO REMANEJAMENTO ###')
print(f'PASTO 1: {pasto_1}')
print(f'PASTO 2: {pasto_2}')
print()

while not len(pasto_2) > len(pasto_1):
    pasto_2.append(pasto_1[0])
    del pasto_1[0]

print('### PASTOS APÓS O REMANEJAMENTO ###')
print(f'PASTO 1: {pasto_1}')
print(f'PASTO 2: {pasto_2}')
