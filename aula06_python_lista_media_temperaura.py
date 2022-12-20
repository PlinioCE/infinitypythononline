# Faça um programa que leia a temperatura média de cada mês de
# determinado ano e armazene-as em uma lista. Após isso, calcule a
# média anual das temperaturas e mostre na tela todas as
# temperaturas acima da média anual e os meses em que ocorreram.

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
temperatura_meses = []
for mes in range(0, 12):
    temperatura_mes = float(input(f'Temperatura(°C) média de {meses[mes]}: '))
    temperatura_meses.append(temperatura_mes)

print()
media_anual_temperatura = sum(temperatura_meses) / len(temperatura_meses)
print(f'MÉDIA ANUAL: {media_anual_temperatura:.1f}°C')

print()
print('MESES COM TEMPERATURA ACIMA DA MÉDIA ANUAL')
contador = 0
for media in temperatura_meses:
    if media > media_anual_temperatura:
        print(f'{meses[contador]}: {temperatura_meses[contador]}°C')
    contador += 1
