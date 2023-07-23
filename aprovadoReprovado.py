#INSERCAO DA NOTAS
nota1 = input('Informe a primeira nota: ')
if float(nota1) > 10 or float(nota1) < 0: 
    nota1 = input('Informe a primeira nota: ')
    
nota2 = input('Informe a segunda nota: ')
if float(nota2) > 10 or float(nota2) < 0: 
    nota2 = input('Informe a segunda nota: ')
    
nota3 = input('Informe a terceira nota: ')
if float(nota3) > 10 or float(nota3) < 0: 
    nota3 = input('Informe a terceira nota: ')
    
nota4 = input('Informe a quarta nota: ')
if float(nota4) > 10 or float(nota4) < 0: 
    nota4 = input('Informe a quarta nota: ')
    
nota5 = input('Informe a quinta nota: ')
if float(nota5) > 10 or float(nota5) < 0: 
    nota5 = input('Informe a quinta nota: ')

#CONVERSAO PARA INTEIRO    
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
nota5 = float(nota5)

total =(nota1+nota2+nota3+nota4+nota5)/5

def checar_aprovacao(nota1, nota2, nota3, nota4, nota5):
    return total >= 7

#CASO SEJA TRUE ESTA APROVADO E SE FOR FALSE ESTA REPROVADO
checagem = checar_aprovacao(nota1, nota2, nota3, nota4, nota5)

if checagem:
    print('APROVADO')
else:
    notaG2 = input('Informe a nota da G2: ')
    notaG2 = float(notaG2)
    if (notaG2+total)/2 >= 5:
        print('APROVADO')
    else:
        print('REPROVADO')

