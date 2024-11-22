import mysql.connector
from src.database.conexao import criar_conexao

def criar_quadra(nomeQuadra, preco, localizacao, descricao):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO quadra (nomeQuadra, preco, localizacao, descricao)
            VALUES (%s, %s, %s, %s)
        """, (nomeQuadra, preco, localizacao, descricao))
        conexao.commit()
        return {"message": "Quadra cadastrado com sucesso"}, 201
    except Exception as erro:
        print(f"Erro ao criar quadra: {erro}")  # Adicione este log para o console
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()


def listar_quadras():
    conexao = None
    cursor = None
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM quadra")
        quadras = cursor.fetchall()
        quadras_list = [{"id": q[0], "nomeQuadra": q[1], "preco": q[2], "localizacao": q[3], "descricao": q[4]} for q in quadras]
        return quadras_list, 200
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def buscar_quadra(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM quadra WHERE id = %s", (id,))
        quadra = cursor.fetchone()
        if quadra:
            quadra_dict = {"id": quadra[0], "nomeQuadra": quadra[1], "preco": quadra[2], "localizacao": quadra[3], "descricao": quadra[4]}
            return quadra_dict, 200
        else:
            return {"error": "Quadra não encontrado"}, 404
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def atualizar_quadra(id, nomeQuadra, preco, localizacao, descricao):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        # Recupera os valores atuais de nomeProduto e preco se não forem fornecidos
        cursor.execute("SELECT nomeQuadra, preco, localizacao, descricao FROM quadra WHERE id = %s", (id,))
        quadra_atual = cursor.fetchone()
        
        if not quadra_atual:
            return {"error": "Quadra não encontrado"}, 404
        
        nomeQuadra = nomeQuadra if nomeQuadra else quadra_atual[0]
        preco = preco if preco else quadra_atual[1]
        localizacao = localizacao if localizacao else quadra_atual[2]
        descricao = descricao if descricao else quadra_atual[3]

        cursor.execute(""" 
            UPDATE quadra
            SET nomeQuadra = %s, preco = %s, localizacao = %s, descricao = %s
            WHERE id = %s
        """, (nomeQuadra, preco, localizacao, descricao, id))
        
        conexao.commit()
        if cursor.rowcount > 0:
            return {"message": "Quadra atualizado com sucesso"}, 200
        else:
            return {"error": "Quadra não encontrado"}, 404
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()


def deletar_quadra(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM quadra WHERE id = %s", (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            return {"message": "Quadra deletado com sucesso"}, 200
        else:
            return {"error": "Quadra nao encontrado"}, 404
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()