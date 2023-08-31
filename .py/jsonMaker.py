import json
import mysql.connector

db_config = mysql.connector.connect(
  host="localhost",
  user="root",
  database="lucas",
  password="root"
)

cursor = db_config.cursor()

cursor.execute("SELECT * FROM pedidos")
pedidos = {"pedidos":[]}

for linha in cursor.fetchall():
    pedidos['pedidos'].append(
        {
            "id": linha[0],
            "id_cliente": linha[1],
            "data_pedido": linha[2],
            "valor_pedido": linha[3]
        }
    )
    
    
with open("Pedidos.json", "w") as arquivo:
    try:    
        json.dump(pedidos, arquivo, indent=4, sort_keys=True, default=str)
    except:
       print(type(pedidos))

print("Connected to database")