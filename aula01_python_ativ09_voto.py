def voto(x):
    """
    Função calcula maioridade eleitoral.
    :param x: ano de nascimento fornecido pelo usuário.
    :return: idade e obrigatoriedade ou não do voto.
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - x
    if 18 <= idade <= 65:
        resp = 'VOTO OBRIGATÓRIO!'
    elif 16 <= idade < 18 and idade > 65:
        resp = 'VOTO OPCIONAL!'
    else:
        resp = 'VOTO NEGADO!'
    return idade, resp


ano_nascimento = int(input('Informe o ano de nascimento: '))
resultado = voto(ano_nascimento)
print(f'\n{resultado}')
