cinturao = []
distancias = []
asteroide = {}

for repeticoes in range(0, 5):
    asteroide.clear()
    nome_asteroide = str(input('Informe o nome do asteróide: ')).upper()
    distancia_asteroide = float(input(f'Informe a distância, em anos-luz, do asteróide: '))
    asteroide = {nome_asteroide: distancia_asteroide}
    distancias.append(distancia_asteroide)
    cinturao.append(asteroide.copy())
    print()
print()
print('ASTERÓIDES REGISTRADOS')
for asteriodes in cinturao:
    print(asteriodes)
print('*' * 80)
print(f'Os asteróides estão a uma distância média de {sum(distancias)/len(cinturao)} anos-luz da Terra.')
