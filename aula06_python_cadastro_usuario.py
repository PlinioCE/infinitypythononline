# Crie um sistema de cadastro de usuários.
# a) As informações são: ID, NOME, CPF, IDADE
# b) Insira 5 usuários no sistema
# c) Altere o nome do usuário número 2
# d) Insira um novo usuário no sistema
# e) Delete o penúltimo usuário


lista_nome = []
lista_id = []
lista_cpf = []
lista_idade = []
id_usuario = 0
while True:
    print('============= CADASTRO =============')
    print('====================================')
    id_usuario += 1
    nome_usuario = str(input('NOME: ')).title()
    cpf_usuario = int(input('CPF(Apenas números): '))
    idade_usuario = int(input('IDADE: '))
    lista_id.append(id_usuario)
    lista_nome.append(nome_usuario)
    lista_cpf.append(cpf_usuario)
    lista_idade.append(idade_usuario)
    lista_usuario = [lista_id, lista_nome, lista_cpf, lista_idade]
    saida = str(input('Deseja realizar novo cadastro? [S/N]: ')).upper()
    print()
    if saida[0] == 'N':
        break
print('============= USUÁRIOS =============')
print('====================================')
for indice in range(0, id_usuario):
    print(f'ID: {lista_id[indice]}\n'
          f'NOME: {lista_nome[indice]}\n'
          f'CPF: {lista_cpf[indice]}\n'
          f'IDADE: {lista_idade[indice]} anos\n')
