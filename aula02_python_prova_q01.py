numero_um = int(input('Informe o 1º número: '))
numero_dois = int(input('Informe o 2º número: '))
while True:
    if numero_dois == numero_um:
        numero_dois = int(input('Informe um número diferente do 1º: '))
    else:
        break

for numero in range(numero_um + 1, numero_dois):
    for primo in range(2, numero):
        if numero % primo == 0:
            break
    else:
        print(f'{numero}', end=' ')
