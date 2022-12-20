nome = str(input('Nome: ')).title()
while len(nome) < 3:
    nome = str(input('Nome: ')).title()
idade = int(input('Idade: '))
while idade not in range(0, 151):
    idade = int(input('Idade: '))
salario = float(input('Salário: R$ '))
while salario <= 0:
    salario = float(input('Salário: R$ '))

sexo = str(input('Sexo[M/F]: ')).upper()
while sexo not in ('M', 'F'):
    sexo = str(input('Sexo[M/F]: ')).upper()
sexo = "Masculino" if sexo == "M" else "Feminino"
estado_civil = str(input('Estado Civil: ')).title()
while estado_civil not in ('Solteiro', 'Solteira', 'Casado', 'Casada', 'Viúvo', 'Viúva', 'Divorciado', 'Divorciada'):
    estado_civil = str(input('Estado Civil: ')).title()
print()
print(f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'Salário: R$ {salario:.2f}\n'
      f'Sexo: {sexo}\n'
      f'Estado Civil: {estado_civil}')
