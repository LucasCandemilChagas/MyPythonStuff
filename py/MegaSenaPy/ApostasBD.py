import mysql.connector
import random
from Apostas import Aposta

class ApostaBD:
    verificaRep = False
    
    #Criacao do banco de dados
    
    def __init__(self):
        self.db_config = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="lucas",
                    password="root"
                    )
        self.tabela = False
    def connectBD(self):
        self.cursorAposta = self.db_config.cursor()
        
    def criarTabela(self):
        if self.tabela is True:
            self.create_table_query = """
                                CREATE TABLE aposta (
                                    id INTEGER PRIMARY KEY NOT NULL
                                    CPF varchar(100) NOT NULL,
                                    nome varchar(100) NOT NULL,
                                    numeros int[] NOT NULL
                                )
                                """
            self.cursorAposta.execute(self.create_table_query)
            print("Criada")
            tabela = True
            
    #insercao de dados no banco
    
    def adicionarNumero(self, aposta, num):
        if type(aposta) is Aposta:
            if type(aposta.numeros) is list[int] and type(num) is int:
                if num in range(1,51) and num not in aposta.numeros:
                    if len(aposta.numeros) < 5:
                        aposta.numeros.append(num)
                    else:
                        self.adicionarNumerosBD(aposta, aposta.numeros)
                else:
                    return False
        return True
    
    def surpresinha(self, aposta):
        if type(aposta) is Aposta:
            aposta.numeros = random.sample(range(1,51),5)
            
    def identificacaoApostador(self, cpf, nome, id):
        apostador = Aposta(cpf, nome, id)
        self.cursorAposta.execute("""
                                    INSERT INTO aposta (id, CPF, nome)
                                    VALUES (%s, %s,%s);
                                    """, (id, cpf, nome))
            
    def adicionarNumerosBD(self, aposta, numeros=None):
        if type(aposta) is Aposta:
                self.cursorAposta.execute("""
                                            SELECT * FROM aposta
                                          """)
                rows = self.cursorAposta.fetchall()
                for row in rows:
                    if row[0] == aposta.id:
                        self.cursorAposta.execute("""
                                    INSERT INTO aposta (numeros)
                                    VALUES (%s);
                                    """, (numeros))
                    
            

         

          
            
                
        