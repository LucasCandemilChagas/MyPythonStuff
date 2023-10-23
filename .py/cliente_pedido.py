import mysql.connector
import random



db_config = mysql.connector.connect(
  host="localhost",
  user="root",
  database="lucas",
  password="root"
)

# Conectando ao banco de dados
cursor = db_config.cursor()
cursorCli = db_config.cursor()
cursorPed = db_config.cursor()

# Comando SQL para criar a tabela
create_table_query = """
CREATE TABLE clientes_pedidos (
    codigo_cliente int NOT NULL PRIMARY KEY,
    qtde_pedidos int,
    total_pedidos decimal(10,2)
)
"""

cursor.execute("""
               DROP TABLE clientes_pedidos
               """)

# Executando o comando SQL para criar a tabela
cursor.execute(create_table_query)
cursorCli.execute("""
               SELECT id FROM clientes
               """)

rows = cursorCli.fetchall()

cursorPed.execute("""
               SELECT * FROM pedidos
               """)

rowsPed = cursorPed.fetchall()

countPedidos = 0
valTotal = 0

for row in rows:
    codCli = row[0]
    countPedidos = 0
    valTotal = 0
    for line in rowsPed: 
        if line[1] == codCli:
           countPedidos+=1
           valTotal = valTotal + line[3]
    cursor.execute("""
    INSERT INTO clientes_pedidos (codigo_cliente, qtde_pedidos,total_pedidos)
    VALUES (%s, %s,%s);
    """, (codCli, countPedidos,valTotal))



# Commit das mudanças e fechamento da conexão
db_config.commit()
db_config.close()

print("Tabela criada com sucesso!")

