import streamlit as st
import pandas as pd

# 1. Estrutura com grupos musculares
GRUPOS_MUSCULARES = {
    "Peito": ["Supino reto barra", "Supino inclinado halteres", "Crucifixo reto", "Crossover no cabo", "Peck deck"],
    "Costas": ["Puxada frente aberta", "Remada curvada", "Puxada neutra", "Remada unilateral", "Pulldown"],
    "Pernas": ["Agachamento livre", "Leg press 45º", "Cadeira extensora", "Mesa flexora", "Stiff"],
    "Ombros": ["Desenvolvimento militar", "Elevação lateral", "Elevação frontal", "Desenvolvimento Arnold", "Crucifixo inverso"],
    "Bíceps": ["Rosca direta barra", "Rosca alternada", "Rosca martelo", "Rosca concentrada", "Rosca Scott"],
    "Tríceps": ["Tríceps corda", "Tríceps testa", "Mergulho banco", "Tríceps coice", "Tríceps polia alta"],
    "Abdômen": ["Abdominal supra", "Abdominal infra", "Prancha", "Abdominal oblíquo", "Abdominal bicicleta"],
    "Glúteos": ["Glúteo no cabo", "Elevação pélvica", "Cadeira abdutora", "Afundo", "Agachamento sumô"]
}

# 2. Função para gerar séries/repetições
def configurar_series_reps(objetivo, experiencia):
    if objetivo == "hipertrofia":
        if experiencia == "iniciante":
            return 3, "12-15"
        elif experiencia == "intermediário":
            return 4, "8-12"
        else:
            return 5, "6-10"
    elif objetivo == "emagrecimento":
        return 3, "15-20"
    elif objetivo == "resistência":
        return 2, "20-25"
    return 3, "12-15"

# 3. Função principal
def exibir_treino(usuario):
    nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino = (
        usuario[1], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7], usuario[8], usuario[9]
    )

    st.title(f"Treino de {nome}")
    st.markdown(f"**Objetivo:** {objetivo.capitalize()} | **Experiência:** {experiencia.capitalize()}")

    series, reps = configurar_series_reps(objetivo, experiencia)

    modo = st.radio("Como deseja montar seu treino semanal?", ["Divisão automática", "Escolher manualmente"])

    plano_treino = {}

    if modo == "Divisão automática":
        grupos = list(GRUPOS_MUSCULARES.keys())
        for i in range(dias_treino):
            grupo = grupos[i % len(grupos)]
            plano_treino[f"Dia {i+1}"] = [grupo]
    else:
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        for i in range(dias_treino):
            with st.expander(f"{dias_semana[i]}"):
                grupos_escolhidos = st.multiselect(
                    f"Grupos musculares para {dias_semana[i]}",
                    options=list(GRUPOS_MUSCULARES.keys()),
                    key=f"dia_{i}"
                )
                if grupos_escolhidos:
                    plano_treino[dias_semana[i]] = grupos_escolhidos

    if plano_treino:
        st.header("Treino Gerado")
        for dia, grupos in plano_treino.items():
            st.subheader(dia)
            for grupo in grupos:
                st.markdown(f"**{grupo}**")
                dados = [{"Exercício": ex, "Séries": series, "Repetições": reps} for ex in GRUPOS_MUSCULARES[grupo]]
                st.dataframe(pd.DataFrame(dados), use_container_width=True)

    st.markdown("---")
    st.markdown("**Lembrete:** Consulte um profissional para acompanhamento individualizado.")

# Exemplo de usuário para teste
usuario = [1, "João", "joao@email.com", 28, 75, 1.78, "masculino", "hipertrofia", "intermediário", 4]
exibir_treino(usuario)
