while True:
    peso_massa = float(input('Informe a massa do material em gramas: '))
    if peso_massa == 0:
        break
    ciclo = 0
    while peso_massa >= 0.1:
        peso_massa = peso_massa - (peso_massa * 0.25)
        ciclo += 1
    print(f'O material levará {ciclo/2}min para atingir uma massa < 0,10g.')
    print()
