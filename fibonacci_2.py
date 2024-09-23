n1 = 0
n2 = 1
n3 = 0
lista = []

numero = int(input('Informe um número: '))

while True:
    lista.append(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3

    if n3 > 10000:
        break

print()
print(lista)
print()
if numero in lista:
    print('Esse número pertence a sequência.')
else:
    print('Esse número não pertence a sequência.')
