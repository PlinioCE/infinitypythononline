# Escreva um programa que peça ao usuário que informe 10
# números inteiros e adicione-os a uma lista.
# Em seguida, percorra toda a lista removendo todos os
# números pares. Por fim, apresente a lista na tela.


# lista = []
# for num in range(1, 11):
#     numero = int(input(f'Digite o {num}º número: '))
#     lista.append(numero)
# print()
# print(f'Lista completa: {lista}')
# lista_par = []
# for indice in range(0, len(lista)):
#     if lista[indice] % 2 == 0:
#         lista_par.append(lista[indice])
# lista = compara_lista
# print()
# print(f'Lista sem pares: {lista}')

lista = []
for num in range(1, 11):
    numero = int(input(f'Digite o {num}º número: '))
    lista.append(numero)
print()
print(f'Lista completa: {lista}')

for revisao in range(4):
    for indice in lista:
        if indice % 2 == 0:
            lista.remove(indice)

print()
print(f'Lista sem pares:{lista}')
