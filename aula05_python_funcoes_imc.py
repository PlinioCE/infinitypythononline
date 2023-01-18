def calcular_imc():
    grupo_nome = []
    grupo_peso = []
    grupo_altura = []
    grupo_imc = []
    for laco in range(1, 5):
        nome = str(input(f'Informe o nome da {laco}ª pessoa: ')).title()
        peso = float(input(f'Informe o peso (kg) da {laco}ª pessoa: '))
        altura = float(input(f'Informe a altura da {laco}ª pessoa: '))
        imc = peso / (altura ** 2)
        grupo_nome.append(nome)
        grupo_peso.append(peso)
        grupo_altura.append(altura)
        grupo_imc.append(round(imc, 2))
    print()
    print('*' * 30)
    for mesclar in zip(grupo_nome, grupo_peso, grupo_altura, grupo_imc):
        print(mesclar)


calcular_imc()
