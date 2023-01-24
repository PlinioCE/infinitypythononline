# calculadora_main.py
from aula06_python_modulos_prova_def_calculadora import *

print('******************************')
print('***** CALCULADORA PYTHON *****')
print('******************************')
print()
numero_um = float(input('Digite o 1º número: '))
numero_dois = float(input('Digite o 2º número: '))
operacao = int(input('Informe a operação que deseja utilizar: \n'
                     '[1] - ADIÇÃO\n'
                     '[2] - SUBTRAÇÃO\n'
                     '[3] - MULTIPLICAÇÃO\n'
                     '[4] - DIVISÃO\n'))
print()
match operacao:
    case 1:
        print(somar(numero_um, numero_dois))
    case 2:
        print(subtrair(numero_um, numero_dois))
    case 3:
        print(multiplicar(numero_um, numero_dois))
    case 4:
        print(dividir(numero_um, numero_dois))
    case _:
        print('Operador inválido!')



