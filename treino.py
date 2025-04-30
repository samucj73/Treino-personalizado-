import streamlit as st
import pandas as pd

# Funções auxiliares para conversão segura
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

# Simulação de banco de dados (exemplo com dicionário)
# Aqui, você substitui com a consulta real ao banco de dados
db_usuarios = {
    1: {
        "nome": "João",
        "idade": 28,
        "peso": 75,
        "altura": 1.78,
        "genero": "masculino",
        "objetivo": "hipertrofia",
        "experiencia": "intermediário",
        "dias_treino": 4
    },
    2: {
        "nome": "Maria",
        "idade": 26,
        "peso": 60,
        "altura": 1.65,
        "genero": "feminino",
        "objetivo": "emagrecimento",
        "experiencia": "iniciante",
        "dias_treino": 3
    }
}

# Função gerar_treino
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

# Função para simular a recuperação do usuário no banco de dados
def obter_usuario_por_id(usuario_id):
    return db_usuarios.get(usuario_id, None)

# Função exibir_treino
def exibir_treino(usuario_id, atualizar_func=lambda *args: None):
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

    with st.form("formulario_edicao"):
        novo_dias_treino = st.number_input("Dias de treino por semana", min_value=1, max_value=7, value=dias_treino)
        if st.form_submit_button("Salvar Alterações"):
            # Atualiza o banco de dados com as alterações
            db_usuarios[usuario_id]["dias_treino"] = novo_dias_treino
            st.success("Perfil atualizado com sucesso!")

    treino = gerar_treino(objetivo, experiencia, novo_dias_treino)

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
