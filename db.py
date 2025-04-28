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

# Função para criar a tabela no banco de dados e garantir que a coluna dias_treino existe
def criar_tabela():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Criação da tabela, se não existir
        criar_tabela_sql = """
        CREATE TABLE IF NOT EXISTS usuariosam (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100),
            senha VARCHAR(100),
            idade INT,
            peso FLOAT,
            altura FLOAT,
            genero VARCHAR(10),
            objetivo VARCHAR(100),
            experiencia VARCHAR(20),
            dias_treino INT
        );
        """
        cursor.execute(criar_tabela_sql)

        # Verificar se a coluna dias_treino já existe, caso contrário, adiciona
        verificar_coluna_sql = """
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM information_schema.columns 
                WHERE table_name='usuariosam' AND column_name='dias_treino'
            ) THEN
                ALTER TABLE usuariosam ADD COLUMN dias_treino INT;
            END IF;
        END $$;
        """
        cursor.execute(verificar_coluna_sql)
        conn.commit()

    except Exception as e:
        raise Exception(f"Ocorreu um erro ao criar a tabela: {e}")
    finally:
        cursor.close()
        conn.close()

# Função para cadastrar usuário
def cadastrar_usuario(nome, senha, idade, peso, altura, genero, objetivo, experiencia):
    conn = get_db_connection()
    cursor = conn.cursor()
    insert_query = sql.SQL("""
        INSERT INTO usuariosam (nome, senha, idade, peso, altura, genero, objetivo, experiencia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """)
    cursor.execute(insert_query, (nome, senha, idade, peso, altura, genero, objetivo, experiencia))
    conn.commit()
    cursor.close()
    conn.close()

# Função para buscar usuário
def obter_usuario(nome, senha):
    conn = get_db_connection()
    cursor = conn.cursor()
    select_query = sql.SQL("SELECT * FROM usuariosam WHERE nome = %s AND senha = %s")
    cursor.execute(select_query, (nome, senha))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return usuario

# Função para atualizar o perfil do usuário
def atualizar_usuario(nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino):
    conn = get_db_connection()
    cursor = conn.cursor()
    update_query = sql.SQL("""
        UPDATE usuariosam 
        SET idade = %s, peso = %s, altura = %s, genero = %s, objetivo = %s, experiencia = %s, dias_treino = %s
        WHERE nome = %s
    """)
    cursor.execute(update_query, (idade, peso, altura, genero, objetivo, experiencia, dias_treino, nome))
    conn.commit()
    cursor.close()
    conn.close()
