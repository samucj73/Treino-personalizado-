from db import cadastrar_usuario, obter_usuario, atualizar_usuario

# Função para cadastro de usuário
def cadastrar(nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    cadastrar_usuario(nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)

# Função para buscar o usuário no banco
def obter(nome, senha):
    return obter_usuario(nome, senha)

# Função para atualizar o perfil do usuário
def atualizar(nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    atualizar_usuario(nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
