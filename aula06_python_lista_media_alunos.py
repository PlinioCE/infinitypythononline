lista_aprovados = []
for aluno in range(1, 11):
    nome_aluno = str(input(f'Digite o nome do {aluno}º aluno: '))
    media_aluno = float(input(f'Digite a média do {aluno}º aluno: '))
    if media_aluno > 7:
        lista_aprovados.append(nome_aluno)
print()
print(f'Lista de aprovados: {lista_aprovados}')
