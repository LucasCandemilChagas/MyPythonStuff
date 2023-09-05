import json
import mysql.connector
import shutil

# Logando ao banco de dados
db_config = mysql.connector.connect(
  host="localhost",
  user="root",
  database="lucas",
  password="root"
)

# Conectando duas vezes ao banco de dados
cursorPed = db_config.cursor(buffered=True)
cursorIPed = db_config.cursor(buffered=True)
cursorCli = db_config.cursor(buffered=True)
cursorProd = db_config.cursor(buffered=True)

cursorPed.execute("SELECT * FROM pedidos order by id_cliente,id")
cursorIPed.execute("SELECT * FROM itens_pedidos")
cursorCli.execute("SELECT * FROM clientes order by id")
cursorProd.execute("SELECT * FROM produtos")

#Armazenando os dados dos dois SELECT para eventos futuros
cP = cursorPed.fetchall()
cI = cursorIPed.fetchall()
cCli = cursorCli.fetchall()
cPr = cursorProd.fetchall()
#Criando json
pedidos = {"pedidos":[]}
j=0

def clienteBD(linha):
    for cli in cCli: 
        if cli[0] == linha[1]:
             pedidos["pedidos"][index]['cliente'].append(
                {
                   'id': cli[0],
                   'nome': cli[1],
                   'sexo': cli[2],
                   'idade': cli[3],
                   'endereco': cli[4]
                }
            )

def prod(line):
    global j
    for p in cPr:
                if p[0] == line[2]:
                    try:
                        pedidos["pedidos"][index]['itens_pedidos'][j]['produto'].append( 
                            {
                                'id': p[0],
                                'descricao': p[1],
                                'estoque': p[2],
                                'valor': p[3]
                            }
                        )
                            
                        #Caso tenha mais de um itens_pedidos o 
                        # incremento abaixo 
                        # garantira que ao fazer o append() acima ele 
                        # colocara o produto no itens_pedidos certo
                        j+=1

                        break
                    
                    except:
                        print('Exception')
                        size = len(pedidos["pedidos"][index]['itens_pedidos'])
                        print(f'Length - {size}  j - {j}')
            
def itens_prod(linha):
    for line in cI:
        if linha[0] == line[1]:
            pedidos["pedidos"][index]['itens_pedidos'].append(
                {
                   'id': line[0],
                   'id_pedido': line[1],
                   #'id_produto': line[2],
                   'produto': [],
                   'qtde': line[3],
                   'valor': line[4]
                }
            )
            #Pega o produto desse line e adiciona
            prod(line)

#Inserindo os dados de cP e cI no json
for index, linha in enumerate(cP):
    pedidos['pedidos'].append( 
        {
            "id": linha[0],
            #"id_cliente": linha[1],
            'cliente': [],
            "data_pedido": linha[2],
            "valor_pedido": linha[3],
            "itens_pedidos": []
        }
    )
    
    clienteBD(linha)
    
    #Percorre o banco de dados itens_pedidos 
    # e adiciona em pedidos["pedidos"][index de linha]['itens_pedidos']
    # os dados de line caso seu id_pedido seja igual a id do BD pedidos
    itens_prod(linha)
    j=0    

#Criando arquivo json   
with open("Pedidos.json", "w") as arquivo:
    try:    
        json.dump(pedidos, arquivo, indent=4, sort_keys=True, default=str)
    except:
       print(type(pedidos))
       
shutil.move("Pedidos.json",'C:\\Users\\lucas\\OneDrive - PUCRS - BR\\Arquivos Aula\\CC\\Projetos\\MyPythonStuff\\.json')

print("Connected to database")