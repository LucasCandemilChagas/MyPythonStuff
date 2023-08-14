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
    descricao char(30),
    estoque int,
    valor decimal(6,2)
)
"""

# Executando o comando SQL para criar a tabela
#cursor.execute(create_table_query)
#j = 200
#for i in range(200):
#    id = j
#    j+=1
#    descricao = gerador.ecommerce_name()
#    estoque = random.randint(5,100)
#    valor = random.uniform(100.00,1000.00)
#    cursor.execute("""
#    INSERT INTO produtos (id, descricao, estoque, valor)
#    VALUES (%s, %s, %s, %s);
#    """, (id, descricao, estoque, valor))




# Commit das mudanças e fechamento da conexão
db_config.commit()
db_config.close()

print("Tabela criada com sucesso!")

    
    
    

