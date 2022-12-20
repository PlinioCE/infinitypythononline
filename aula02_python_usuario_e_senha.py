while True:
    print('------------ TELA DE LOGIN -----------')
    confirma_cadastro = str(input('Já possui cadastro na plataforma? [S/N]: ')).upper()
    if confirma_cadastro[0] == 'S':
        login = str(input('Login: '))
        senha = str(input('Senha: '))
        if senha == login:
            print('SENHA INCORRETA')
            senha = str(input('Senha: '))
        print('ACESSO PERMITIDO')
        break
    elif confirma_cadastro[0] == 'N':
        print('---------- TELA DE CADASTRO ----------')
        nome = str(input('Nome completo: '))
        email = str(input('E-mail: '))
        login = str(input('Login: '))
        senha = str(input('Senha: '))
        while senha == login:
            print('Senha não pode ser igual ao Login')
            senha = str(input('Senha: '))
        if senha != login:
            confirma_senha = str(input('Confirmação de senha: '))
            while senha != confirma_senha:
                print('Senhas não combinam')
                confirma_senha = str(input('Confirmação de senha: '))
        print('CADASTRO REALIZADO COM SUCESSO!')
