import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from treino import gerar_treino_personalizado

# Função para prever evolução do treino com base nos dados de dias de treino
def sugestao_treino_ia(usuario):
    dados_treino = pd.DataFrame({
        'dias_treino': [2, 3, 4, 5, 6],
        'peso_suplemento': [40, 45, 50, 55, 60]  # Exemplo fictício de aumento de peso no supino (kg)
    })

    X = dados_treino[['dias_treino']]
    y = dados_treino['peso_suplemento']
    modelo = LinearRegression()
    modelo.fit(X, y)

    previsao_peso = modelo.predict(np.array([[usuario['dias_treino']]]))

    return previsao_peso[0]

# Função para ajustar o treino com base no objetivo do usuário
def ajustar_treino_ia(usuario, treino):
    if usuario['objetivo'] == "Ganhar massa muscular":
        for dia, exercicios in treino.items():
            for ex in exercicios:
                ex['séries'] += 1  # Aumentando séries
                ex['repetições'] += 2  # Aumentando repetições
    return treino

# Função para exibir a aba de IA
def exibir_ia(usuario):
    if 'usuario' not in st.session_state:
        st.error("Usuário não encontrado na sessão. Faça login novamente.")
        st.stop()

    st.title(f"Inteligência Artificial - Sugestões de Treino para {usuario['nome']}")

    tabs = st.tabs(["📋 Análise de Evolução", "🏋️ Ajustes no Treino", "📊 Análises Corporais Avançadas"])

    with tabs[0]:
        st.subheader("Previsão de Evolução do Treino")
        previsao = sugestao_treino_ia(usuario)
        st.write(f"A previsão de aumento de peso no supino após {usuario['dias_treino']} dias de treino é: **{previsao:.2f} kg**")

    with tabs[1]:
        st.subheader("Ajuste no Treino Baseado em IA")
        st.write("A IA pode ajustar o seu treino com base no seu objetivo. Se o seu objetivo é ganhar massa muscular, ela aumenta a intensidade e o volume do treino.")

        if st.button("Ativar Inteligência Artificial para Ajustar Treino"):
            # Verifica se os dados estão completos
            campos_necessarios = ['objetivo', 'experiencia', 'dias_treino', 'grupos_musculares']
            if all(campo in usuario for campo in campos_necessarios):
                treino_gerado = gerar_treino_personalizado(
                    usuario['objetivo'],
                    usuario['experiencia'],
                    usuario['dias_treino'],
                    usuario['grupos_musculares']
                )
                treino_ajustado = ajustar_treino_ia(usuario, treino_gerado)

                st.success("Treino ajustado com sucesso!")
                for dia, exercicios in treino_ajustado.items():
                    with st.expander(dia):
                        st.markdown(f"### {dia}")
                        for ex in exercicios:
                            st.markdown(f"**{ex['nome']}**")
                            st.write(f"- Séries: {ex['séries']}")
                            st.write(f"- Repetições: {ex['repetições']}")
                            st.write(f"- Equipamento: {ex['equipamento']}")
            else:
                st.error("Preencha todos os dados do treino na aba 'Treino' antes de usar a IA.")
        else:
            st.info("Clique no botão acima para ativar a inteligência artificial.")

    with tabs[2]:
        st.subheader("Análises Corporais Avançadas")
        st.write("Aqui a IA analisa os dados do seu corpo e faz recomendações mais precisas de treino e nutrição.")
        st.markdown(f"**Recomendação de Proteína Diária (com IA):** {usuario['peso'] * 1.5:.2f}g")
        st.markdown(f"**Recomendação de Carboidrato (com IA):** {usuario['peso'] * 2.0:.2f}g")
