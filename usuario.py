from db import cadastrar_usuario, obter_usuario, atualizar_usuario, recuperar_por_email

def cadastrar(nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    try:
        cadastrar_usuario(nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
    except Exception as e:
        raise Exception(f"Erro ao cadastrar: {e}")

def obter(nome, senha):
    try:
        return obter_usuario(nome, senha)
    except Exception as e:
        raise Exception(f"Erro ao obter usuário: {e}")

def atualizar(id_usuario, nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    try:
        atualizar_usuario(id_usuario, nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
    except Exception as e:
        raise Exception(f"Erro ao atualizar usuário: {e}")

def recuperar_credencial(email):
    try:
        return recuperar_por_email(email)
    except Exception as e:
        raise Exception(f"Erro ao recuperar credenciais: {e}")
