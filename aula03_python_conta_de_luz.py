contador_residencial = contador_comercial = contador_industrial = 0
consumo_residencial = consumo_comercial = consumo_industrial = 0
while True:
    print('------------------ ENEL CEARÁ ------------------')
    print('------------------------------------------------')
    numero_consumidor = int(input('Número do consumidor: '))
    if numero_consumidor == 0:
        print('ENCERRANDO SISTEMA!')
        break
    consumo_kwh = int(input('Consumo kW/mês: '))
    tipo_consumidor = int(input('TIPO CONSUMIDOR:\n'
                                '[1] - Residencial\n'
                                '[2] - Comercial\n'
                                '[3] - Industrial\n'))
    print()
    if tipo_consumidor == 1:
        valor_residencial = consumo_kwh * 0.3
        consumidor_residencial = numero_consumidor
        consumo_residencial += consumo_kwh
        contador_residencial += 1
        print('------------------ ENEL CEARÁ ------------------')
        print('-------------------- FATURA --------------------')
        media_residencial = consumo_residencial / contador_residencial
        print(f'Consumidor Residencial: Nº {consumidor_residencial}\n'
              f'TOTAL A PAGAR: R$ {valor_residencial:.2f}\n')
    elif tipo_consumidor == 2:
        valor_comercial = consumo_kwh * 0.5
        consumidor_comercial = numero_consumidor
        consumo_comercial += consumo_kwh
        contador_comercial += 1
        print('------------------ ENEL CEARÁ ------------------')
        print('-------------------- FATURA --------------------')
        media_comercial = consumo_comercial / contador_comercial
        print(f'Consumidor Comercial: Nº {consumidor_comercial}\n'
              f'TOTAL A PAGAR: R$ {valor_comercial:.2f}')
    elif tipo_consumidor == 3:
        valor_industrial = consumo_kwh * 0.7
        consumidor_industrial = numero_consumidor
        consumo_industrial += consumo_kwh
        contador_industrial += 1
        print('------------------ ENEL CEARÁ ------------------')
        print('-------------------- FATURA --------------------')
        print(f'Consumidor Industrial: Nº {consumidor_industrial}\n'
              f'TOTAL A PAGAR: R$ {valor_industrial:.2f}')
    else:
        print('Tipo de consumidor não encontrado.')

print()
print('------------------ ENEL CEARÁ ------------------')
print('------------------- RELATÓRIO ------------------')
print(f'Consumo total Residencial: {consumo_residencial} kW/mês.')
print(f'Consumo total Comercial: {consumo_comercial} kW/mês.')
print(f'Consumo total Industrial: {consumo_industrial} kW/mês.')
print(f'Média consumo Residencial: {media_residencial} kW.')
print(f'Média consumo Comercial: {media_comercial} kW.')
