# usuario.py

usuarios = {}

def cadastrar_usuario(nome, email, senha, idade, peso, altura, objetivo, experiencia):
    if email in usuarios:
        return False, "Usuário já cadastrado"
    usuarios[email] = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "objetivo": objetivo,
        "experiencia": experiencia,
    }
    return True, "Usuário cadastrado com sucesso"

def autenticar_usuario(email, senha):
    if email in usuarios and usuarios[email]["senha"] == senha:
        return True, usuarios[email]
    return False, "Credenciais inválidas"

def atualizar_dados_usuario(email, **kwargs):
    if email not in usuarios:
        return False, "Usuário não encontrado"
    for chave, valor in kwargs.items():
        if chave in usuarios[email]:
            usuarios[email][chave] = valor
    return True, "Dados atualizados com sucesso"
