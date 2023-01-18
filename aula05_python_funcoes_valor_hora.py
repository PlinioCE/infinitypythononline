def calcular_valor_hora(salario):
    valor_dia = salario / 22
    valor_hora = valor_dia / 8
    return round(valor_hora, 2)


nome = str(input('Informe o nome do(a) funcionário(a): ')).title()
salario = float(input('Informe o salário do(a) funcionário(a): R$ '))
print()
print(f'O valor da hora do Sr(a). {nome} é de R$ {calcular_valor_hora(salario)}.')
