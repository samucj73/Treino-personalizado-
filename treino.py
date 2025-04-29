import streamlit as st
import pandas as pd

# 1. Função gerar_treino
def gerar_treino(usuario):
    objetivo = usuario[7]
    return f"Treino personalizado focado em **{objetivo.capitalize()}**!"

# 2. Função exibir_treino
def exibir_treino(usuario, atualizar_func):
    treino = gerar_treino(usuario)
    st.markdown(treino)

    # Extrair dados do usuário
    nome = usuario[1]  # Nome
    idade = usuario[3]
    peso = usuario[4]
    altura = usuario[5]
    genero = usuario[6]
    objetivo = usuario[7]
    experiencia = usuario[8]
    dias_treino = usuario[9]  # Agora temos dias_treino

    # Exibir as informações para edição
    with st.form("formulario_edicao"):
        novo_dias_treino = st.number_input("Dias de treino por semana", min_value=1, max_value=7, value=dias_treino)
        if st.form_submit_button("Salvar Alterações"):
            # Atualiza o perfil com o novo número de dias de treino
            atualizar_func(nome, idade, peso, altura, genero, objetivo, experiencia, novo_dias_treino)
            st.success("Perfil atualizado com sucesso!")

    st.subheader("Resumo de Saúde")

    # Definir séries, repetições, descanso e peso com base no objetivo e experiência
    if objetivo == "hipertrofia":
        if experiencia == "iniciante":
            series, reps, descanso, peso_treino = 3, "12-15", "60s", "moderado"
        elif experiencia == "intermediário":
            series, reps, descanso, peso_treino = 4, "8-12", "60-90s", "pesado"
        else:
            series, reps, descanso, peso_treino = 5, "6-10", "90s", "muito pesado"
    elif objetivo == "emagrecimento":
        series, reps, descanso, peso_treino = 3, "15-20", "30-45s", "leve"
    elif objetivo == "resistência":
        series, reps, descanso, peso_treino = 2, "20-25", "30s", "médio"
    else:
        series, reps, descanso, peso_treino = 3, "12-15", "60s", "moderado"  # Padrão

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
        df = pd.DataFrame([{"Exercício": ex, "Séries": series, "Repetições": reps, "Peso recomendado": peso_treino} for ex in exercicios])
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

# Exemplo de uso para teste local
usuario = [1, "Nome", "email@example.com", 30, 70, 1.75, "masculino", "hipertrofia", "intermediário", 4] 
#exibir_treino(usuario)
