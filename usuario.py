# usuario.py

import uuid

usuarios = {}

def cadastrar(nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    if email in usuarios:
        raise ValueError("Usuário já cadastrado com este e-mail.")

    usuario_id = str(uuid.uuid4())
    usuarios[email] = {
        "id": usuario_id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "genero": genero,
        "objetivo": objetivo,
        "experiencia": experiencia,
        "dias_treino": dias_treino
    }

def obter(nome, senha):
    for usuario in usuarios.values():
        if usuario["nome"] == nome and usuario["senha"] == senha:
            return usuario
    return None

def atualizar(usuario_id, nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    for usuario in usuarios.values():
        if usuario["id"] == usuario_id:
            usuario.update({
                "nome": nome,
                "idade": idade,
                "peso": peso,
                "altura": altura,
                "genero": genero,
                "objetivo": objetivo,
                "experiencia": experiencia,
                "dias_treino": dias_treino
            })
            return
    raise ValueError("Usuário não encontrado.")

def recuperar_senha(email):
    if email in usuarios:
        return f"Sua senha é: {usuarios[email]['senha']}"
    else:
        raise ValueError("E-mail não cadastrado.")
