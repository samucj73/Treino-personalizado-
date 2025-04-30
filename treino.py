import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Conectar ao banco de dados (ajustar para seu banco real)
engine = create_engine('sqlite:///meu_banco.db')  # Substitua para o banco que você está utilizando

# Função auxiliar para garantir a recuperação de dados com falhas seguras
def to_int(valor, default=0):
    try:
        return int(valor)
    except (TypeError, ValueError):
        return default

def to_float(valor, default=0.0):
    try:
        return float(valor)
    except (TypeError, ValueError):
        return default

# Função para obter os dados do usuário no banco de dados
def obter_usuario_por_id(usuario_id):
    with engine.connect() as conn:
        # Recuperar o usuário por ID
        resultado = conn.execute(f"SELECT * FROM usuarios WHERE id = {usuario_id}")
        usuario = resultado.fetchone()
        if usuario:
            return dict(usuario)
        else:
            return None

# Função de treino que usa os dados recuperados
def gerar_treino(objetivo, experiencia, dias_treino):
    if objetivo == "hipertrofia":
        if experiencia == "iniciante":
            series, reps = 3, "12-15"
        elif experiencia == "intermediário":
            series, reps = 4, "8-12"
        else:
            series, reps = 5, "6-10"
    elif objetivo == "emagrecimento":
        series, reps = 3, "15-20"
    elif objetivo == "resistência":
        series, reps = 2, "20-25"
    else:
        series, reps = 3, "12-15"

    treino = {
        "Peito": {
            "exercicios": [
                "Supino reto com barra",
                "Supino inclinado com halteres",
                "Crucifixo reto",
                "Crossover no cabo",
                "Peck deck"
            ],
            "séries": series,
            "repetições": reps
        },
        "Costas": {
            "exercicios": [
                "Puxada frente aberta",
                "Remada curvada",
                "Remada unilateral com halteres",
                "Remada baixa",
                "Pulldown com pegada neutra"
            ],
            "séries": series,
            "repetições": reps
        },
        "Pernas": {
            "exercicios": [
                "Agachamento livre",
                "Leg press 45º",
                "Cadeira extensora",
                "Mesa flexora",
                "Stiff com halteres"
            ],
            "séries": series,
            "repetições": reps
        },
        "Ombros": {
            "exercicios": [
                "Desenvolvimento militar",
                "Elevação lateral",
                "Elevação frontal",
                "Desenvolvimento Arnold",
                "Crucifixo inverso na máquina"
            ],
            "séries": series,
            "repetições": reps
        },
        "Glúteos": {
            "exercicios": [
                "Agachamento sumô com halteres",
                "Elevação de quadril no banco",
                "Afundo com halteres",
                "Extensão de quadril no cabo",
                "Ponte de glúteo solo"
            ],
            "séries": series,
            "repetições": reps
        }
    }

    return treino

# Função para atualizar o banco de dados com os dados de treino (caso seja necessário)
def atualizar_usuario(usuario_id, dias_treino):
    with engine.connect() as conn:
        # Atualiza os dados do usuário no banco
        conn.execute(f"UPDATE usuarios SET dias_treino = {dias_treino} WHERE id = {usuario_id}")

# Função para exibir o treino e informações do usuário
def exibir_treino(usuario_id):
    usuario = obter_usuario_por_id(usuario_id)
    
    if not usuario:
        st.error("Usuário não encontrado.")
        return

    nome = usuario["nome"]
    idade = usuario["idade"]
    peso = usuario["peso"]
    altura = usuario["altura"]
    genero = usuario["genero"]
    objetivo = usuario["objetivo"]
    experiencia = usuario["experiencia"]
    dias_treino = usuario["dias_treino"]

    st.header(f"Treino personalizado para {nome}")

    # Formulário para editar os dados do treino
    with st.form("formulario_edicao"):
        novo_dias_treino = st.number_input("Dias de treino por semana", min_value=1, max_value=7, value=dias_treino)
        if st.form_submit_button("Salvar Alterações"):
            # Atualiza os dados no banco de dados
            atualizar_usuario(usuario_id, novo_dias_treino)
            st.success("Perfil atualizado com sucesso!")

    treino = gerar_treino(objetivo, experiencia, novo_dias_treino)

    # Exibindo as informações do usuário
    st.subheader("Dados do Usuário")
    st.markdown(f"""
    - **Idade:** {idade} anos  
    - **Peso:** {peso:.1f} kg  
    - **Altura:** {altura:.2f} m  
    - **Gênero:** {genero.capitalize()}  
    - **Objetivo:** {objetivo.capitalize()}  
    - **Experiência:** {experiencia.capitalize()}  
    """)

    st.divider()
    st.header("Treino por Grupo Muscular")

    # Exibindo o treino gerado
    for musculo, dados in treino.items():
        with st.expander(f"{musculo}"):
            st.markdown(f"**Séries:** {dados['séries']} | **Repetições:** {dados['repetições']}")
            for i, ex in enumerate(dados["exercicios"], start=1):
                st.markdown(f"{i}. {ex}")

    st.divider()
    st.subheader("Orientações Gerais")
    st.markdown(f"""
    - **Aquecimento:** Faça 5 a 10 minutos antes do treino.  
    - **Descanso entre séries:** 30s a 90s dependendo da intensidade.  
    - **Alongamento:** Recomendado após o treino.  
    - **Progresso:** Aumente a carga gradualmente com técnica adequada.  
    - Consulte um profissional para ajustes personalizados.
    """)

# Exemplo para teste local
usuario_id = 1  # Simula a busca de um usuário específico no banco de dados
exibir_treino(usuario_id)
