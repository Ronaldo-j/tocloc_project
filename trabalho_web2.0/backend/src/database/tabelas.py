def criar_tabelas(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
        id INT auto_increment PRIMARY KEY,
        nomeUsuario VARCHAR(100) NOT NULL,
        email VARCHAR(200) NOT NULL,
        password VARCHAR(50) NOT NULL
        )
    """)