import mysql.connector
import os
from dotenv import load_dotenv
from src.database.tabelas import criar_tabelas

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

def criar_conexao():
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conexao.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS user")
        cursor.execute("USE user")
        criar_tabelas(cursor)
    except Exception as erro:
        print(f"{erro}: Erro ao criar o banco de dados")
    return conexao