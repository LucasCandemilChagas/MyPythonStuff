notas = []
cont = 0
checagem = True
#FUNCAO PARA INSERCAO DA NOTAS
def def_notas():
    nota = ' '
    if not checagem:
        nota = input('Informe a nota da G2: ')
    else:
        nota = input(f'Informe sua {cont+1}a nota: ') 
    while not nota.isnumeric():
        nota = input('Valor informado nao eh um numero positivo! Digite novamente: ')
    while float(nota) > 10:
        nota = input('Nota infomada nao esta entre 0 e 10! Digite novamente: ')
        while not nota.isnumeric():
            nota = input('Valor informado nao eh um numero positivo! Digite novamente: ')  
    return float(nota)

t = 5
while t:
    notas.append(def_notas())
    cont+=1
    t-=1

total = (notas[0]+notas[1]+notas[2]+notas[3]+notas[4])/5

#RETORNA TRUE OU FALSE
def checar_aprovacao():
    return total >= 7

checagem = checar_aprovacao()

#CASO SEJA TRUE ESTA APROVADO E SE FOR FALSE ESTA REPROVADO
if checagem:
    print(f'Media {total} - APROVADO')
else:
    notaG2 = def_notas()
    if (notaG2+total)/2 >= 5:
        print(f'Media {notaG2} - APROVADO')
    else:
        print(f'Media {notaG2} - REPROVADO')

