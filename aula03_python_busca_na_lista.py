lista = []
contador = 1
while contador <= 15:
    numero = int(input(f'Digite o {contador}º número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Número já existe!')
        continue
    contador += 1
lista.sort()
busca_numero = int(input('Digite o número que deseja buscar: '))
if busca_numero in lista:
    print(f'O número {busca_numero} está no índice {lista.index(busca_numero)} da lista.')
print()
print(f'Confira a lista: {lista}')
