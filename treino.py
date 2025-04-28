import streamlit as st
import pandas as pd

# Função para gerar treino
def gerar_treino(usuario):
    idade = usuario[3]
    peso = usuario[4]
    altura = usuario[5]
    genero = usuario[6].lower()
    objetivo = usuario[7].lower()
    experiencia = usuario[8].lower()

    # Definir séries, repetições e descanso com base no objetivo e experiência
    if objetivo == "hipertrofia":
        if experiencia == "iniciante":
            series, reps, descanso = 3, "12-15", "60s"
        elif experiencia == "intermediário":
            series, reps, descanso = 4, "8-12", "60-90s"
        else:
            series, reps, descanso = 5, "6-10", "90s"
    elif objetivo == "emagrecimento":
        series, reps, descanso = 3, "15-20", "30-45s"
    elif objetivo == "resistência":
        series, reps, descanso = 2, "20-25", "30s"
    else:
        series, reps, descanso = 3, "12-15", "60s"  # Padrão

    # Mostrar dados físicos
    st.header("Dados do Usuário")
    st.markdown(f"""
    - **Idade:** {idade} anos  
    - **Peso:** {peso:.1f} kg  
    - **Altura:** {altura:.2f} m  
    - **Gênero:** {genero.capitalize()}  
    - **Objetivo:** {objetivo.capitalize()}  
    - **Experiência:** {experiencia.capitalize()}  
    """)

    st.divider()
    st.header("Treino Semanal")

    # Função auxiliar para criar tabela
    def criar_tabela(exercicios):
        df = pd.DataFrame([{"Exercício": ex, "Séries": series, "Repetições": reps} for ex in exercicios])
        st.dataframe(df, use_container_width=True)

    # Treinos por dia
    with st.expander("Segunda-feira (Peito e Tríceps)"):
        criar_tabela([
            "Supino reto barra",
            "Supino inclinado halteres",
            "Crucifixo reto",
            "Crossover no cabo",
            "Tríceps testa",
            "Tríceps corda"
        ])

    with st.expander("Terça-feira (Costas e Bíceps)"):
        criar_tabela([
            "Puxada frente aberta",
            "Remada baixa",
            "Puxada frente neutra",
            "Remada unilateral",
            "Rosca direta barra",
            "Rosca alternada halteres"
        ])

    with st.expander("Quarta-feira (Pernas e Abdômen)"):
        criar_tabela([
            "Agachamento livre",
            "Leg press 45º",
            "Cadeira extensora",
            "Mesa flexora",
            "Stiff com halteres",
            "Glúteo no cabo",
            "Abdominal supra solo (3x20)",
            "Prancha isométrica (3x30s)",
            "Abdominal oblíquo solo (3x20 cada lado)"
        ])

    with st.expander("Quinta-feira (Ombros e Trapézio)"):
        criar_tabela([
            "Desenvolvimento militar",
            "Elevação lateral",
            "Elevação frontal",
            "Encolhimento de ombros",
            "Desenvolvimento Arnold",
            "Crucifixo inverso máquina"
        ])

    with st.expander("Sexta-feira (Glúteos e Abdômen)"):
        if genero == "feminino":
            criar_tabela([
                "Agachamento sumô com halteres",
                "Elevação de quadril no banco",
                "Afundo com halteres",
                "Abdução de quadril máquina",
                "Ponte de glúteo solo",
                "Extensão de quadril no cabo",
                "Abdominal infra solo (3x20)",
                "Prancha lateral (3x30s)",
                "Abdominal bicicleta (3x20)"
            ])
        else:
            criar_tabela([
                "Agachamento frontal barra",
                "Agachamento búlgaro halteres",
                "Leg press 45º",
                "Extensão de quadril no cabo",
                "Cadeira abdutora",
                "Elevação de quadril solo",
                "Abdominal supra banco (3x20)",
                "Prancha lateral (3x30s)",
                "Abdominal infra no banco (3x20)"
            ])

    st.divider()
    st.subheader("Orientações Importantes")
    st.markdown(f"""
    - **Descanso entre séries:** {descanso}  
    - **Alongamento** após os treinos é recomendado.  
    - Realize os exercícios com a **técnica correta** para evitar lesões.  
    - **Progresso:** aumente cargas gradativamente conforme evolução.  
    - **Aquecimento:** 5-10 minutos antes de começar.  
    - **Dica:** Consulte um profissional de educação física para ajustes personalizados!
    """)

# Exemplo de uso
usuario = [1, "Nome", "email@example.com", 30, 70, 1.75, "masculino", "hipertrofia", "intermediário"]
gerar_treino(usuario)
