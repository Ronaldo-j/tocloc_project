import mysql.connector
from src.database.conexao import criar_conexao

def criar_reserva(user_id, quadra_id, horario):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO reserva (user_id, quadra_id, horario)
            VALUES (%s, %s, %s)
        """, (user_id, quadra_id, horario))
        conexao.commit()
        return {"message": "Reserva criada com sucesso."}, 201
    except mysql.connector.IntegrityError as e:
        if "Duplicate entry" in str(e):
            return {"error": "A quadra já está reservada neste horário. Por favor, escolha outro horário."}, 400
        return {"error": "Erro ao criar reserva."}, 500
    except Exception as erro:
        conexao.rollback()
        print(f"Erro inesperado ao criar reserva: {erro}")  # Adicione um log
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()



def listar_reservas():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT r.id, r.user_id, r.quadra_id, r.horario, u.nomeUsuario, q.nomeQuadra
            FROM reserva r
            JOIN user u ON r.user_id = u.id
            JOIN quadra q ON r.quadra_id = q.id
        """)
        reservas = cursor.fetchall()
        reservas_list = [
            {
                "id": r[0],
                "user_id": r[1],
                "quadra_id": r[2],
                "horario": r[3],
                "nomeUsuario": r[4],
                "nomeQuadra": r[5]
            } for r in reservas
        ]
        return reservas_list, 200
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def buscar_reserva(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT r.id, r.user_id, r.quadra_id, r.horario, u.nomeUsuario, q.nomeQuadra
            FROM reserva r
            JOIN user u ON r.user_id = u.id
            JOIN quadra q ON r.quadra_id = q.id
            WHERE r.id = %s
        """, (id,))
        reserva = cursor.fetchone()
        if reserva:
            reserva_dict = {
                "id": reserva[0],
                "user_id": reserva[1],
                "quadra_id": reserva[2],
                "horario": reserva[3],
                "nomeUsuario": reserva[4],
                "nomeQuadra": reserva[5]
            }
            return reserva_dict, 200
        else:
            return {"error": "Reserva não encontrada."}, 404
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def atualizar_reserva(id, user_id, quadra_id, horario):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        # Verifica se a reserva existe
        cursor.execute("SELECT id FROM reserva WHERE id = %s", (id,))
        if not cursor.fetchone():
            return {"error": "Reserva não encontrada."}, 404

        cursor.execute("""
            UPDATE reserva
            SET user_id = %s, quadra_id = %s, horario = %s
            WHERE id = %s
        """, (user_id, quadra_id, horario, id))
        conexao.commit()
        return {"message": "Reserva atualizada com sucesso."}, 200
    except mysql.connector.IntegrityError as e:
        if "Duplicate entry" in str(e):
            return {"error": "A quadra já está reservada neste horário."}, 400
        return {"error": str(e)}, 500
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def deletar_reserva(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM reserva WHERE id = %s", (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            return {"message": "Reserva deletada com sucesso."}, 200
        else:
            return {"error": "Reserva não encontrada."}, 404
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()
