import psycopg2
from psycopg2 import sql

# Nome da tabela
NOME_TABELA = "alunos"

# Função para conectar ao banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="dpg-d06oq3qli9vc73ejebbg-a",
        database="sal_6scc",
        user="sal_6scc_user",
        password="NT5pmK5SWCB0voVzFqRkofj8YVKjL3Q1"
    )
    return conn

# Função para criar a tabela (com campo email)
def criar_tabela():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        criar_tabela_sql = sql.SQL("""
            CREATE TABLE IF NOT EXISTS {table} (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) UNIQUE,
                email VARCHAR(100) UNIQUE,
                senha VARCHAR(100),
                idade INT,
                peso FLOAT,
                altura FLOAT,
                genero VARCHAR(10),
                objetivo VARCHAR(100),
                experiencia VARCHAR(20),
                dias_treino INT
            )
        """).format(table=sql.Identifier(NOME_TABELA))

        cursor.execute(criar_tabela_sql)
        conn.commit()
    except Exception as e:
        raise Exception(f"Erro ao criar a tabela: {e}")
    finally:
        cursor.close()
        conn.close()

# Verificar se usuário já existe
def usuario_existe(nome):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = sql.SQL("SELECT 1 FROM {table} WHERE nome = %s").format(
            table=sql.Identifier(NOME_TABELA)
        )
        cursor.execute(query, (nome,))
        return cursor.fetchone() is not None
    finally:
        cursor.close()
        conn.close()

# Cadastrar usuário (com e-mail)
def cadastrar_usuario(nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    if usuario_existe(nome):
        raise ValueError(f"O usuário '{nome}' já existe.")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = sql.SQL("""
            INSERT INTO {table} (nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """).format(table=sql.Identifier(NOME_TABELA))
        
        cursor.execute(query, (nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino))
        conn.commit()
    except Exception as e:
        raise Exception(f"Erro ao cadastrar usuário: {e}")
    finally:
        cursor.close()
        conn.close()

# Obter usuário por nome e senha
def obter_usuario(nome, senha):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = sql.SQL("""
            SELECT * FROM {table}
            WHERE nome = %s AND senha = %s
        """).format(table=sql.Identifier(NOME_TABELA))

        cursor.execute(query, (nome, senha))
        return cursor.fetchone()
    except Exception as e:
        raise Exception(f"Erro ao obter usuário: {e}")
    finally:
        cursor.close()
        conn.close()

# Atualizar dados do usuário
def atualizar_usuario(id_usuario, nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = sql.SQL("""
            UPDATE {table}
            SET nome = %s, idade = %s, peso = %s, altura = %s, genero = %s,
                objetivo = %s, experiencia = %s, dias_treino = %s
            WHERE id = %s
        """).format(table=sql.Identifier(NOME_TABELA))
        
        cursor.execute(query, (nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino, id_usuario))
        conn.commit()
    except Exception as e:
        raise Exception(f"Erro ao atualizar usuário: {e}")
    finally:
        cursor.close()
        conn.close()

# Recuperar login/senha por e-mail
def recuperar_por_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = sql.SQL("""
            SELECT nome, senha FROM {table}
            WHERE email = %s
        """).format(table=sql.Identifier(NOME_TABELA))
        
        cursor.execute(query, (email,))
        return cursor.fetchone()  # (nome, senha) ou None
    except Exception as e:
        raise Exception(f"Erro ao recuperar por email: {e}")
    finally:
        cursor.close()
        conn.close()
