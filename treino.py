import streamlit as st

# Função para gerar treino
def gerar_treino(usuario):
    idade = usuario[3]
    peso = usuario[4]
    altura = usuario[5]
    genero = usuario[6].lower()
    objetivo = usuario[7].lower()
    experiencia = usuario[8].lower()

    # Definir séries e repetições
    if genero == "masculino":
        if experiencia == "iniciante":
            series = 3
            reps = "12-15"
        elif experiencia == "intermediário":
            series = 4
            reps = "8-12"
        else:  # avançado
            series = 5
            reps = "6-10"
    else:  # feminino
        if experiencia == "iniciante":
            series = 3
            reps = "15-20"
        elif experiencia == "intermediário":
            series = 4
            reps = "12-15"
        else:  # avançado
            series = 5
            reps = "8-12"

    treino = f"## Dados Físicos\n"
    treino += f"- **Idade:** {idade} anos\n"
    treino += f"- **Peso:** {peso:.1f} kg\n"
    treino += f"- **Altura:** {altura:.2f} m\n"
    treino += f"- **Gênero:** {genero.capitalize()}\n"
    treino += f"- **Objetivo:** {objetivo.capitalize()}\n"
    treino += f"- **Experiência:** {experiencia.capitalize()}\n"
    treino += "---\n\n"

    treino += "## Treino Semanal\n"

    # Segunda-feira (Peito e Tríceps)
    treino_segunda = f"""
### Segunda-feira (Peito e Tríceps)
- Supino reto barra ({series}x{reps}) - Banco + Barra
- Supino inclinado halteres ({series}x{reps}) - Banco + Halteres
- Crucifixo reto ({series}x{reps}) - Banco + Halteres
- Crossover no cabo ({series}x{reps}) - Cross Over
- Tríceps testa ({series}x{reps}) - Barra W
- Tríceps corda ({series}x{reps}) - Polia
"""
    
    # Terça-feira (Costas e Bíceps)
    treino_terca = f"""
### Terça-feira (Costas e Bíceps)
- Puxada frente aberta ({series}x{reps}) - Cross Over
- Remada baixa ({series}x{reps}) - Máquina Remada
- Puxada frente neutra ({series}x{reps}) - Cross Over
- Remada unilateral ({series}x{reps}) - Halteres
- Rosca direta barra ({series}x{reps}) - Barra Reta
- Rosca alternada halteres ({series}x{reps}) - Halteres
"""

    # Quarta-feira (Pernas e Abdômen)
    treino_quarta = f"""
### Quarta-feira (Pernas e Abdômen)
- Agachamento livre ({series}x{reps}) - Barra
- Leg press 45º ({series}x{reps}) - Leg Press
- Cadeira extensora ({series}x{reps}) - Máquina
- Mesa flexora ({series}x{reps}) - Máquina
- Stiff com halteres ({series}x{reps}) - Halteres
- Glúteo cabo ({series}x{reps}) - Polia (principalmente para feminino)

- Abdominal supra solo (3x20) - Peso corporal
- Prancha isométrica (3x30s) - Colchonete
- Abdominal oblíquo solo (3x20 cada lado) - Peso corporal
"""

    # Quinta-feira (Ombros e Trapézio)
    treino_quinta = f"""
### Quinta-feira (Ombros e Trapézio)
- Desenvolvimento militar ({series}x{reps}) - Barra ou Halteres
- Elevação lateral ({series}x{reps}) - Halteres
- Elevação frontal ({series}x{reps}) - Halteres
- Encolhimento de ombros ({series}x{reps}) - Barra
- Desenvolvimento Arnold ({series}x{reps}) - Halteres
- Crucifixo inverso máquina ({series}x{reps}) - Máquina de deltoide posterior
"""

    # Sexta-feira (Glúteos e Abdômen)
    if genero == "feminino":
        treino_sexta = f"""
### Sexta-feira (Glúteos e Abdômen)
- Agachamento sumô com halteres ({series}x{reps}) - Halteres
- Elevação de quadril no banco ({series}x{reps}) - Banco + Peso
- Afundo com halteres ({series}x{reps}) - Halteres
- Abdução de quadril máquina ({series}x{reps}) - Máquina
- Ponte de glúteo solo ({series}x{reps}) - Peso corporal
- Extensão de quadril no cabo ({series}x{reps}) - Polia

- Abdominal infra solo (3x20) - Peso corporal
- Prancha lateral (3x30s) - Colchonete
- Abdominal bicicleta (3x20) - Peso corporal
"""
    else:
        treino_sexta = f"""
### Sexta-feira (Glúteos e Abdômen)
- Agachamento frontal barra ({series}x{reps}) - Barra
- Agachamento búlgaro halteres ({series}x{reps}) - Halteres
- Levantamento terra ({series}x{reps}) - Barra
- Mesa flexora ({series}x{reps}) - Máquina
- Glúteo 4 apoios caneleira ({series}x{reps}) - Caneleira
- Stiff barra ({series}x{reps}) - Barra

- Abdominal infra solo (3x20) - Peso corporal
- Prancha lateral (3x30s) - Colchonete
- Abdominal bicicleta (3x20) - Peso corporal
"""

    treino += treino_segunda + treino_terca + treino_quarta + treino_quinta + treino_sexta

    treino += "\n---\n"
    treino += "_Recomendamos avaliação médica antes de iniciar atividades físicas._\n"

    treino += f"\n**Observação:** Este treino foi adaptado para **{genero.capitalize()} {experiencia.capitalize()}** visando **{objetivo.capitalize()}**.\n"

    return treino


# Função para exibir treino no Streamlit com linhas e colunas
def exibir_treino(usuario):
    treino = gerar_treino(usuario)

    # Exibindo os dados físicos em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**Idade:** {usuario[3]} anos")
        st.markdown(f"**Peso:** {usuario[4]:.1f} kg")
        st.markdown(f"**Altura:** {usuario[5]:.2f} m")
    
    with col2:
        st.markdown(f"**Gênero:** {usuario[6].capitalize()}")
        st.markdown(f"**Objetivo:** {usuario[7].capitalize()}")
        st.markdown(f"**Experiência:** {usuario[8].capitalize()}")

    st.markdown("---")

    # Dividindo o treino semanal por dia
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(treino_segunda)
        st.markdown(treino_quarta)
        st.markdown(treino_sexta)

    with col2:
        st.markdown(treino_terca)
        st.markdown(treino_quinta)
