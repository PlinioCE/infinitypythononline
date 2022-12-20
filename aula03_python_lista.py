lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'Lista original: {lista}')
lista.reverse()
print(f'Lista reversa: {lista}')
lista.sort()
lista.append(27)
print(f'Add 27 ao fim da lista: {lista}')
lista.remove(9)
print(f'Excluindo o número 9: {lista}')
lista.pop(8)
print(f'Apagando a posição 10: {lista}')
print(f'Somando os elementos: {sum(lista)}')
print(f'Maior elemento: {max(lista)}')
lista_pares = []
for pares in lista:
    if pares % 2 == 0:
        lista_pares.append(pares)
print(f'Números pares: {lista_pares}')
