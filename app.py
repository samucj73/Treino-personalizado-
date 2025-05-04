import streamlit as st
import random
from exercicios import EXERCICIOS

def gerar_treino(grupo_muscular, dias, volume, intensidade, experiencia):
    plano = {}
    num_exercicios_por_dia = {
        'iniciante': 3,
        'intermediario': 5,
        'avancado': 6
    }[experiencia]

    for dia in range(1, dias + 1):
        dia_treino = []

        for grupo in grupo_muscular:
            todos = []
            for nivel in ['iniciante', 'intermediario', 'avancado']:
                if experiencia == "iniciante" and nivel == "iniciante":
                    todos.extend(EXERCICIOS.get(grupo, {}).get(nivel, []))
                elif experiencia == "intermediario" and nivel in ["iniciante", "intermediario"]:
                    todos.extend(EXERCICIOS.get(grupo, {}).get(nivel, []))
                elif experiencia == "avancado":
                    todos.extend(EXERCICIOS.get(grupo, {}).get(nivel, []))

            escolhidos = random.sample(todos, min(num_exercicios_por_dia, len(todos)))

            for ex in escolhidos:
                dia_treino.append({
                    "grupo": grupo.capitalize(),
                    "nome": ex['nome'],
                    "series": ex['series'],
                    "repeticoes": ex['repeticoes'],
                    "equipamento": ex['equipamento']
                })

        plano[f"Dia {dia}"] = dia_treino

    return plano

# Interface Streamlit
st.set_page_config(page_title="App de Treino", layout="centered")
st.title("Gerador de Plano de Treino Personalizado")

# Menu lateral
aba = st.sidebar.selectbox("Escolha uma funcionalidade", ["Gerar Treino"])

if aba == "Gerar Treino":
    st.header("Configurações do Treino")

    grupos = st.multiselect("Grupos Musculares", list(EXERCICIOS.keys()), default=["peito", "costas"])
    dias = st.slider("Dias de treino por semana", 1, 7, 3)
    volume = st.selectbox("Volume do treino", ["baixo", "médio", "alto"])
    intensidade = st.selectbox("Intensidade do treino", ["baixa", "média", "alta"])
    experiencia = st.selectbox("Nível de experiência", ["iniciante", "intermediario", "avancado"])

    if st.button("Gerar Plano"):
        if not grupos:
            st.warning("Selecione ao menos um grupo muscular.")
        else:
            plano = gerar_treino(grupos, dias, volume, intensidade, experiencia)

            st.success("Plano de treino gerado com sucesso!")
            for dia, exercicios in plano.items():
                st.markdown(f"## {dia}")
                for ex in exercicios:
                    st.markdown(
                        f"- **{ex['grupo']}** | **{ex['nome']}**  \n"
                        f"  Séries: {ex['series']} | Repetições: {ex['repeticoes']} | Equipamento: {ex['equipamento']}"
                    )
