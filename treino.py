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

    # Aqui poderia haver lógica para distribuir os exercícios entre os dias de treino
    treino_dividido = dividir_treino_por_dia(treino, dias_treino)

    return treino_dividido

def dividir_treino_por_dia(treino, dias_treino):
    treino_dividido = {}
    musculos = list(treino.keys())

    for i, musculo in enumerate(musculos):
        treino_dividido[musculo] = {
            "exercicios": treino[musculo]["exercicios"],
            "séries": treino[musculo]["séries"],
            "repetições": treino[musculo]["repetições"]
        }
    
    # Aqui pode-se fazer uma distribuição mais sofisticada dos treinos por dias
    return treino_dividido

# Função exibir_treino
def exibir_treino(usuario, atualizar_func=lambda *args: None):
    nome = usuario[1]
    idade = to_int(usuario[3], default=25)
    peso = to_float(usuario[4], default=70.0)
    altura = to_float(usuario[5], default=1.70)
    genero = usuario[6]
    objetivo = usuario[7]
    experiencia = usuario[8]
    dias_treino = to_int(usuario[9], default=3)

    st.header(f"Treino personalizado para {nome}")

    with st.form("formulario_edicao"):
        novo_dias_treino = st.number_input("Dias de treino por semana", min_value=1, max_value=7, value=dias_treino)
        if st.form_submit_button("Salvar Alterações"):
            atualizar_func(nome, idade, peso, altura, genero, objetivo, experiencia, novo_dias_treino)
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
usuario = [1, "João", "joao@email.com", "28", 75, 1.78, "masculino", "hipertrofia", "intermediário", 4]
exibir_treino(usuario)
