import uuid
from db import cadastrar_usuario, obter_usuario, atualizar_usuario, recuperar_por_email

def cadastrar(nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    # Usando a função do db.py para cadastrar usuário
    try:
        cadastrar_usuario(nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
    except ValueError as e:
        raise e
    except Exception as e:
        raise Exception(f"Erro ao cadastrar usuário: {e}")

def obter(nome_ou_email, senha):
    # Usando a função do db.py para obter o usuário
    usuario = obter_usuario(nome_ou_email, senha)
    if usuario:
        return usuario
    return None

def atualizar(usuario_id, nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    try:
        atualizar_usuario(usuario_id, nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
    except Exception as e:
        raise Exception(f"Erro ao atualizar usuário: {e}")

def recuperar_senha(email):
    # Usando a função do db.py para recuperar a senha
    resultado = recuperar_por_email(email)
    if resultado:
        return f"Sua senha é: {resultado[1]}"
    else:
        raise ValueError("E-mail não cadastrado.")
