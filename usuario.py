from db import cadastrar_usuario, obter_usuario, atualizar_usuario

def cadastrar(nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    try:
        cadastrar_usuario(nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
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
