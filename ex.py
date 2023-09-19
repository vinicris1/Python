"""
produtos = [1] * 10

descontado = 0
y = 0
valor = 0


while produtos[y] != 0:
    if y == 9:
        break
    else:

        y = y + 1
        produtos[y] = int(input('Digite o produto numero {}: '.format(y)))
        if produtos[y] >= 500 and produtos[y] < 1000:

            print('desconto de 5% aplicado')
            descontado = produtos[y] * 0.95
            valor = valor + (produtos[y] - descontado)
            print('Valor com desconto = {}'.format(descontado))


        if produtos[y] >= 1000:
            print("desconto 10% aplicado")
            descontado = produtos[y] * 0.90
            valor = valor + (produtos[y] - descontado)
            print('Valor com desconto = {}'.format(descontado))

else:
    print("Quantidade de clientes = {}".format(y))
    print("Desconto total foi de {} reais" .format(valor))
    print("stop")

print("Fim do dia")
print("Quantidade de desconto total = {}".format(valor))
print("Total de clientes = {}".format(y - 1))
"""

#resposta transferida de visualg para python, melhor...
"""
conta = 0
compra = 1
totaldescontos = 0

while compra != 0:

    compra = float(input('Digite o produto = '))
    desconto = 0
    if compra >= 1000:
        desconto = compra * 0.1
    
    if compra >= 500 and compra < 1000:
        desconto = compra * 0.05
    
    print("Desconto: {}".format(desconto))
    totaldescontos = totaldescontos + desconto

    if desconto > 0:
        conta = conta + 1
    
print("Clientes atendidos: {}".format(conta))
print("Total de desconto concedido: {}".format(totaldescontos))
"""
"""
x = 4
b = 8
n = 6

while x < b:
    n = n + b
    x = n-(x*2)

b = (x-n)*4

print("x = {}".format(x))
print("b = {}".format(b))
print("n = {}".format(n))
"""
"""
i = 0
j = 0
k = 0

for i in range(5): 
    j = j + 1
    for k in range(j):
        print("*")
    #print('*')
"""

val = int(input('Digite um valor inteiro: '))

a = val
b = val

for P in range(7):
    if(a>=val) and (val != 0):
        a = (val + b) - a
    if((b < val) and (val != 0)):
        b = (val + a) - b
    val = int(input('Digite um valor inteiro: '))

print("a: {}".format(a))
print("b: {}".format(b))