numero = int(input('Digite um número: '))
soma = 0
for num in range(0, numero):
    num += 1
    soma += num
    if num == numero:
        print(num, end=' = ')
    else:
        print(num, end='+')
print(soma)
