def mensagem(nome, saudacao='Boa aula'):
    """
    Função saúda aluno.
    :param nome: nome do aluno
    :param saudacao: padrão
    :return: saudação
    """
    if nome == '':
        nome = 'Fulaninho de Tal'
    print(f'\n{saudacao}, {nome}.')


nome_aluno = str(input('Informe seu nome: ')).strip().title()
mensagem(nome_aluno)
