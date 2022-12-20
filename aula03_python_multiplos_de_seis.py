lista = []
lista_seis = []
contador = 0
while contador < 6:
    contador += 1
    numero = int(input(f'Digite o {contador}º número: '))
    lista.append(numero)
    if numero % 6 == 0:
        lista_seis.append(numero)
print(f'Lista: {lista}')
print(f'Multiplos de 6: {lista_seis}')
