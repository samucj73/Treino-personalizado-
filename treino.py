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

# Dicionário de exercícios e equipamentos
EXERCICIOS_E_EQUIPAMENTOS = {
    "Supino reto com barra": "Banco reto + Barra olímpica",
    "Supino inclinado com halteres": "Banco inclinado + Halteres",
    "Crucifixo reto": "Banco reto + Halteres",
    "Crossover no cabo": "Máquina de crossover (cabos)",
    "Peck deck": "Máquina peck deck",
    "Puxada frente aberta": "Máquina de puxada alta",
    "Remada curvada": "Barra ou barra T",
    "Remada unilateral com halteres": "Halter + banco",
    "Remada baixa": "Máquina de remada baixa",
    "Pulldown com pegada neutra": "Máquina ou puxador com pegada neutra",
    "Agachamento livre": "Barra + Rack de agachamento",
    "Leg press 45º": "Máquina de leg press",
    "Cadeira extensora": "Máquina extensora",
    "Mesa flexora": "Máquina flexora",
    "Stiff com halteres": "Halteres",
    "Desenvolvimento militar": "Máquina ou barra",
    "Elevação lateral": "Halteres",
    "Elevação frontal": "Halteres ou barra",
    "Desenvolvimento Arnold": "Halteres",
    "Crucifixo inverso na máquina": "Máquina peck deck reversa",
    "Agachamento sumô com halteres": "Halter ou kettlebell",
    "Elevação de quadril no banco": "Banco + peso livre",
    "Afundo com halteres": "Halteres",
    "Extensão de quadril no cabo": "Cabo com tornozeleira",
    "Ponte de glúteo solo": "Peso corporal ou barra"
}

# Função para gerar treino baseado no perfil
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

    grupos = {
        "A - Peito e Tríceps": [
            "Supino reto com barra", "Supino inclinado com halteres",
            "Crucifixo reto", "Peck deck", "Crossover no cabo"
        ],
        "B - Costas e Bíceps": [
            "Puxada frente aberta", "Remada curvada",
            "Remada unilateral com halteres", "Remada baixa", "Pulldown com pegada neutra"
        ],
        "C - Pernas e Glúteos": [
            "Agachamento livre", "Leg press 45º", "Cadeira extensora",
            "Mesa flexora", "Stiff com halteres"
        ],
        "D - Ombros e Abdômen": [
            "Desenvolvimento militar", "Elevação lateral", "Desenvolvimento Arnold",
            "Crucifixo inverso na máquina", "Elevação frontal"
        ]
    }

    dias_disponiveis = list(grupos.items())[:dias_treino]

    treino_dividido = {}
    for dia_nome, exercicios in dias_disponiveis:
        treino_dividido[dia_nome] = {
            "séries": series,
            "repetições": reps,
            "exercicios": [
                {
                    "nome": ex,
                    "equipamento": EXERCICIOS_E_EQUIPAMENTOS.get(ex, "Equipamento não especificado")
                }
                for ex in exercicios
            ]
        }

    return treino_dividido

# Função principal para exibir o treino com Streamlit
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

    # Formulário para alterar número de dias de treino
    with st.form("formulario_edicao"):
        novo_dias_treino = st.number_input("Dias de treino por semana", min_value=1, max_value=7, value=dias_treino)
        if st.form_submit_button("Salvar Alterações"):
            atualizar_func(nome, idade, peso, altura, genero, objetivo, experiencia, novo_dias_treino)
            st.success("Perfil atualizado com sucesso!")

    treino = gerar_treino(objetivo, experiencia, novo_dias_treino)

    # Exibir dados do usuário
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
    st.header("Treino por Dia")

    # Exibir treino dividido por grupo
    for grupo, dados in treino.items():
        with st.expander(grupo):
            st.markdown(f"**Séries:** {dados['séries']} | **Repetições:** {dados['repetições']}")
            for i, ex in enumerate(dados["exercicios"], start=1):
                st.markdown(f"""{i}. **{ex['nome']}**  
> Equipamento: *{ex['equipamento']}*""")

    st.divider()
    st.subheader("Orientações Gerais")
    st.markdown("""
    - **Aquecimento:** Faça 5 a 10 minutos antes do treino.  
    - **Descanso entre séries:** 30s a 90s dependendo da intensidade.  
    - **Alongamento:** Recomendado após o treino.  
    - **Progresso:** Aumente a carga gradualmente com técnica adequada.  
    - Consulte um profissional para ajustes personalizados.
    """)

# Exemplo para teste local
if __name__ == "__main__":
    usuario = [1, "João", "joao@email.com", "28", 75, 1.78, "masculino", "hipertrofia", "intermediário", 4]
    exibir_treino(usuario)
