import mysql.connector
from src.database.conexao import criar_conexao

def criar_user(nomeUsuario, email, password):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO user (nomeUsuario, email, password)
            VALUES (%s, %s, %s)
        """,(nomeUsuario, email, password)), 
        conexao.commit()
        return {"message": "usuario cadastrado com sucesso"}, 201
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def listar_user():
    conexao = None
    cursor = None
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM user")
        user = cursor.fetchall()
        user_list = [{"id": u[0], "nomeUsuario": u[1], "email": u[2], "password": u[3]} for u in user]
        return user_list, 200
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        
def buscar_user(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM user WHERE id = %s", (id,))
        user = cursor.fetchone()
        if user:
            user_dict = {"id": user[0], "nomeUser": user[1], "email": user[2], "password": user[3]}
            return user_dict, 200
        else:
            return {"error": "Usuario não encontrado"}, 404
    except Exception as erro:
        return{"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def atualizar_user(id, nomeUsuario, email, password):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute("SELECT nomeUsuario, email, password FROM user WHERE id = %s", (id,))
        user_atual = cursor.fetchone()

        if not user_atual:
            return {"error": "Usuario não encontrado"}, 404
        
        nomeUsuario = nomeUsuario if nomeUsuario else user_atual[0]
        email = email if email else user_atual[1]
        password = password if password else user_atual[2]

        cursor.execute("""
            UPDATE user
            SET nomeUsuario = %s, email = %s, password = %s
            WHERE id = %s
        """, (nomeUsuario, email, password, id))

        conexao.commit()
        if cursor.rowcount >0:
            return {"message": "Usuario atualizado com sucesso"}, 200
        else:
            return {"erro": "Usuario não encontrado"}, 404
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def deletar_user(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            return {"message": "Usuario deletado com sucesso"}, 200
        else:
            return{"error": "Usuario não encontrado"}, 404
    
    except Exception as erro:
        conexao.rollback()
        return{"erro": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()