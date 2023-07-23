#INSERCAO DA NOTAS
nota1 = float(input('Informe a primeira nota: '))
if nota1 > 10 or nota1 < 0: 
    nota1 = float(input('Informe a primeira nota: '))
    
nota2 = float(input('Informe a segunda nota: '))
if nota2 > 10 or nota2 < 0: 
    nota2 = float(input('Informe a segunda nota: '))
    
nota3 = float(input('Informe a terceira nota: '))
if nota3 > 10 or nota3 < 0: 
    nota3 = float(input('Informe a terceira nota: '))
    
nota4 = float(input('Informe a quarta nota: '))
if nota4 > 10 or nota4 < 0: 
    nota4 = float(input('Informe a quarta nota: '))
    
nota5 = float(input('Informe a quinta nota: '))
if nota5 > 10 or nota5 < 0: 
    nota5 = float(input('Informe a quinta nota: '))

total =(nota1+nota2+nota3+nota4+nota5)/5

def checar_aprovacao(nota1, nota2, nota3, nota4, nota5):
    return total >= 7

#CASO SEJA TRUE ESTA APROVADO E SE FOR FALSE ESTA REPROVADO
checagem = checar_aprovacao(nota1, nota2, nota3, nota4, nota5)

if checagem:
    print('APROVADO')
else:
    notaG2 = float(input('Informe a nota da G2: '))
    if (notaG2+total)/2 >= 5:
        print('APROVADO')
    else:
        print('REPROVADO')

