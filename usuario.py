from db import cadastrar_usuario, obter_usuario

# Função para cadastro de usuário
def cadastrar(nome, senha, idade, peso, altura, genero, objetivo, experiencia):
    cadastrar_usuario(nome, senha, idade, peso, altura, genero, objetivo, experiencia)

# Função para buscar o usuário no banco
def obter(nome, senha):
    return obter_usuario(nome, senha)
