import psycopg2
from psycopg2 import sql

# Função para conectar ao banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="dpg-d06oq3qli9vc73ejebbg-a",
        database="sal_6scc",
        user="sal_6scc_user",
        password="NT5pmK5SWCB0voVzFqRkofj8YVKjL3Q1"
    )
    return conn

# Função para criar a tabela
def criar_tabela(nome_tabela):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        criar_tabela_sql = f"""
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) UNIQUE, -- já garantindo que nomes sejam únicos
            senha VARCHAR(100),
            idade INT,
            peso FLOAT,
            altura FLOAT,
            genero VARCHAR(10),
            objetivo VARCHAR(100),
            experiencia VARCHAR(20)
            -- dias_treino adicionado abaixo
        );
        """
        cursor.execute(criar_tabela_sql)
        conn.commit()

        # Verifica se a coluna 'dias_treino' existe
        cursor.execute(f"""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = '{nome_tabela}' AND column_name = 'dias_treino'
        """)
        coluna = cursor.fetchone()

        if not coluna:
            cursor.execute(f"ALTER TABLE {nome_tabela} ADD COLUMN dias_treino INT;")
            conn.commit()

    except Exception as e:
        raise Exception(f"Ocorreu um erro ao criar a tabela: {e}")
    finally:
        cursor.close()
        conn.close()

# Função para verificar se o usuário já existe
def usuario_existe(nome_tabela, nome):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql.SQL(f"SELECT 1 FROM {nome_tabela} WHERE nome = %s"), (nome,))
    existe = cursor.fetchone()
    cursor.close()
    conn.close()
    return existe is not None

# Função para cadastrar usuário
def cadastrar_usuario(nome_tabela, nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    if usuario_existe(nome_tabela, nome):
        raise ValueError(f"O usuário '{nome}' já existe.")

    conn = get_db_connection()
    cursor = conn.cursor()
    insert_query = sql.SQL(f"""
        INSERT INTO {nome_tabela} (nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """)
    cursor.execute(insert_query, (nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino))
    conn.commit()
    cursor.close()
    conn.close()

# Função para buscar usuário
def obter_usuario(nome_tabela, nome, senha):
    conn = get_db_connection()
    cursor = conn.cursor()
    select_query = sql.SQL(f"SELECT * FROM {nome_tabela} WHERE nome = %s AND senha = %s")
    cursor.execute(select_query, (nome, senha))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return usuario

# Função para atualizar perfil
def atualizar_usuario(nome_tabela, nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    conn = get_db_connection()
    cursor = conn.cursor()
    update_query = sql.SQL(f"""
        UPDATE {nome_tabela}
        SET idade = %s, peso = %s, altura = %s, genero = %s, objetivo = %s, experiencia = %s, dias_treino = %s
        WHERE nome = %s
    """)
    cursor.execute(update_query, (idade, peso, altura, genero, objetivo, experiencia, dias_treino, nome))
    conn.commit()
    cursor.close()
    conn.close()
