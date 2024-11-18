def criar_tabelas(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
        id INT auto_increment PRIMARY KEY,
        nomeUsuario VARCHAR(100) NOT NULL,
        email VARCHAR(200) NOT NULL,
        password VARCHAR(50) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quadra (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nomeQuadra VARCHAR(100) NOT NULL,
        preco DOUBLE NOT NULL,
        localizacao VARCHAR(200) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reserva (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        quadra_id INT NOT NULL,
        horario DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (quadra_id) REFERENCES quadra(id),
        UNIQUE (quadra_id, horario) -- Garante que a mesma quadra não possa ser reservada no mesmo horário
        )
    """)