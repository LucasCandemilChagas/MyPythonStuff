import mysql.connector
import random
import faker
import openpyxl
import faker_commerce

gerador = faker.Faker()

gerador.add_provider(faker_commerce.Provider)

db_config = mysql.connector.connect(
  host="localhost",
  user="root",
  database="lucas",
  password="root"
)

# Conectando ao banco de dados
cursor = db_config.cursor()

# Comando SQL para criar a tabela
create_table_query = """
CREATE TABLE itens_pedidos (
    id int AUTO_INCREMENT PRIMARY KEY,
    id_pedido int,
    id_produto int,
    qtde int,
    valor decimal(6,2)
)
"""

# Executando o comando SQL para criar a tabela
cursor.execute("""
               DROP TABLE itens_pedidos
               """)
cursor.execute(create_table_query)
j = 200
for i in range(200):
    id_produto = random.randint(200,400)
    id_pedido = random.randint(6000,6999)
    qtde = random.randint(1,10)
    valor = 0
    cursor.execute("""
    INSERT INTO itens_pedidos (id_produto,id_pedido, qtde, valor)
    VALUES (%s, %s, %s, %s);
    """, (id_produto, id_pedido, qtde, valor))



# Commit das mudanças e fechamento da conexão
db_config.commit()
db_config.close()

print("Tabela criada com sucesso!")

    
    
    

