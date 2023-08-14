import mysql.connector
import random
import faker
import openpyxl

gerador = faker.Faker()
    

db_config = mysql.connector.connect(
  host="localhost",
  user="root",
  database="lucas",
  password="root"
)

# Conectando ao banco de dados
cursor = db_config.cursor()

# Comando SQL para criar a tabela
#create_table_query = """
#CREATE TABLE pedidos (
#    id int AUTO_INCREMENT PRIMARY KEY,
#    id_cliente int,
#    data_pedido date,
#    valor_pedido decimal(10,2)
#)
#"""

# Executando o comando SQL para criar a tabela
#cursor.execute(create_table_query)

for i in range(1, 1001):
    id_cliente = random.randint(1, 100)
    data_pedido = gerador.date()
    valor_pedido = random.uniform(1.00, 1000.00)
    cursor.execute("""
    INSERT INTO pedidos (id_cliente, data_pedido, valor_pedido)
    VALUES (%s, %s, %s);
    """, (id_cliente, data_pedido, valor_pedido))




# Commit das mudanças e fechamento da conexão
db_config.commit()
db_config.close()

print("Tabela criada com sucesso!")

