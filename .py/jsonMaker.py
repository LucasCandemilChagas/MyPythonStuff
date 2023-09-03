import json
import mysql.connector

db_config = mysql.connector.connect(
  host="localhost",
  user="root",
  database="lucas",
  password="root"
)

cursor = db_config.cursor(buffered=True)
cursor1 = db_config.cursor(buffered=True)

cursor.execute("SELECT * FROM pedidos")
cursor1.execute("SELECT * FROM itens_pedidos")

c = cursor.fetchall()
c1 = cursor1.fetchall()

pedidos = {"pedidos":[]}
i=0

for linha in c:
    pedidos['pedidos'].append( 
        {
            "id": linha[0],
            "id_cliente": linha[1],
            "data_pedido": linha[2],
            "valor_pedido": linha[3],
            "itens_pedidos": []
        }
    )
    for line in c1:
        if linha[0] == line[1]:
            pedidos["pedidos"][i]['itens_pedidos'].append(
                {
                   'id': line[0],
                   'id_pedido': line[1],
                   'id_produto': line[2],
                   'qtde': line[3],
                   'valor': line[4]
                }
            )
    i+=1
    
with open("Pedidos.json", "w") as arquivo:
    try:    
        json.dump(pedidos, arquivo, indent=4, sort_keys=True, default=str)
    except:
       print(type(pedidos))

print("Connected to database")