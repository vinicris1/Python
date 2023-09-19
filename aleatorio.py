import random

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(lista)

escolhido = random.choice(lista)
print(escolhido)