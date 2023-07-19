lista = [2,5,6,1,7,10,8,9,3,4]
maior = 0
menor = lista[0]
for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
print(maior)
print(menor)
