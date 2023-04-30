#passo 1: criar a lista
cocos_e_pedras={}

#passo 2: ler o arquivo
arquivo=open('C:\\Users\\lucas\\OneDrive - PUCRS - BR\\Arquivos Aula\\CC\\Projetos\\MyPythonStuff\\trabGauterio\\caso0050.txt')
#passo 3: ler cada linha dos cocos e pedras
for linha in arquivo:
    print(linha[0])
    cocos_e_pedras[linha[0]]= linha[:11]
#passo 4: ler o input   
macacos = input("digite algo:")
resultado=""
#passo 5: ler a linhas passo a passo ate achar o resultado
for pedras in macacos.replace(" ", "").lower():
    resultado += cocos_e_pedras[pedras]
print("numero de macacos:", macacos)
print("numero de pedras:", resultado)
print("resultado final:", len(resultado))