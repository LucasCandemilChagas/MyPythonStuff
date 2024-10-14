import random
dados = []
def inserirDados():
    nome = input('Insira o nome: ')
    try:
        id = int(input('Insira o id: '))
    except:
        id = random.randint(1,1000)
    endereco = input('Insira o endereco: ')
    dado =  id, nome, endereco 
    dados.append(dado)
    
tab_on = True



while tab_on:
    
    inserirDados()

    tab_off = input('Queres inserir mais dados? y/n: ')
    if tab_off == 'n':
        tab_on = False


print('-========================================-')
for i in dados:
    print(f'id = {i[0]}; nome = {i[1]}; endereco = {i[2]};')
print('-========================================-')