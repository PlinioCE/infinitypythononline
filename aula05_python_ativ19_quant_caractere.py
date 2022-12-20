def quant_letras(x):
    x = x.replace(' ', '')
    x = len(x)
    return x


frase = str(input('Escreva uma frase: '))
resultado = quant_letras(frase)
print(f'\nNa frase existe {resultado} letras.')
