#INSERCAO DA NOTAS
nota1 = input('Informe a primeira nota: ')
if int(nota1) > 10 or int(nota1) < 0: 
    nota1 = input('Informe a primeira nota: ')
    
nota2 = input('Informe a segunda nota: ')
if int(nota2) > 10 or int(nota2) < 0: 
    nota2 = input('Informe a segunda nota: ')
    
nota3 = input('Informe a terceira nota: ')
if int(nota3) > 10 or int(nota3) < 0: 
    nota3 = input('Informe a terceira nota: ')
    
nota4 = input('Informe a quarta nota: ')
if int(nota4) > 10 or int(nota4) < 0: 
    nota4 = input('Informe a quarta nota: ')
    
nota5 = input('Informe a quinta nota: ')
if int(nota5) > 10 or int(nota5) < 0: 
    nota5 = input('Informe a quinta nota: ')

#CONVERSAO PARA INTEIRO    
nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)
nota4 = int(nota4)
nota5 = int(nota5)

total =(nota1+nota2+nota3+nota4+nota5)/5

def checar_aprovacao(nota1, nota2, nota3, nota4, nota5):
    return total >= 7

#CASO SEJA TRUE ESTA APROVADO E SE FOR FALSE ESTA REPROVADO
checagem = checar_aprovacao(nota1, nota2, nota3, nota4, nota5)

if checagem:
    print('APROVADO')
else:
    notaG2 = input('Informe a nota da G2: ')
    notaG2 = int(notaG2)
    if (notaG2+total)/2 >= 5:
        print('APROVADO')
    else:
        print('REPROVADO')

