import sqlite3
import os

# Garante que a pasta 'data' existe antes de criar o banco de dados
os.makedirs("data", exist_ok=True)

# Caminho completo para o banco de dados dentro da pasta data
DB_PATH = "data/imoveis.db"

def conectar():
    """Retorna uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(DB_PATH)

def criar_tabelas():
    """Cria a tabela inicial para armazenar os dados dos imóveis."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imoveis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            bairro TEXT,
            preço REAL,
            aluguel REAL,
            rentabilidade REAL
        )
    """)
    conn.commit()
    conn.close()
    print("Banco de dados e tabela criados com sucesso na pasta data!")

if __name__ == "__main__":
    criar_tabelas()

