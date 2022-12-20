def tempo(dd, mm, aaaa):
    """
    Função calcula a quantidade de dias em que uma determinada data, informada pelo usuário, aconteceu
    :param dd: valor de dois dígitos para o dia
    :param mm: valor de dois dígitos para o mês
    :param aaaa: valor de quatro dígitos para o ano
    :return: a quantidade de dias passados até a data atual
    """
    from datetime import date
    dia_atual = date.today().day
    mes_atual = date.today().month
    ano_atual = date.today().year
    dias = abs(dia_atual - dd)
    meses = abs(mes_atual - mm)
    anos = abs(ano_atual - aaaa)
    dias *= 24
    meses *= 24 * 30
    anos *= 24 * 365.25
    tempo_total = dias + meses + anos
    return tempo_total / 24


d = int(input('Informe o dia(dd): '))
m = int(input('Informe o mês(mm): '))
a = int(input('Informe o ano(aaaa): '))
resultado = tempo(d, m, a)
print(f'\nO dia {d}/{m}/{a} aconteceu há {resultado:.0f} dias.')
