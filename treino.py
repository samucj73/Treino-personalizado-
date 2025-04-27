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

    treino += """
### Segunda-feira (Peito e Tríceps)
- Supino reto barra ({}x{}) - Banco + Barra
- Supino inclinado halteres ({}x{}) - Banco + Halteres
- Crucifixo reto ({}x{}) - Banco + Halteres
- Crossover no cabo ({}x{}) - Cross Over
- Tríceps testa ({}x{}) - Barra W
- Tríceps corda ({}x{}) - Polia

### Terça-feira (Costas e Bíceps)
- Puxada frente aberta ({}x{}) - Cross Over
- Remada baixa ({}x{}) - Máquina Remada
- Puxada frente neutra ({}x{}) - Cross Over
- Remada unilateral ({}x{}) - Halteres
- Rosca direta barra ({}x{}) - Barra Reta
- Rosca alternada halteres ({}x{}) - Halteres

### Quarta-feira (Pernas e Abdômen)
- Agachamento livre ({}x{}) - Barra
- Leg press 45º ({}x{}) - Leg Press
- Cadeira extensora ({}x{}) - Máquina
- Mesa flexora ({}x{}) - Máquina
- Stiff com halteres ({}x{}) - Halteres
- Glúteo cabo ({}x{}) - Polia (principalmente para feminino)

- Abdominal supra solo (3x20) - Peso corporal
- Prancha isométrica (3x30s) - Colchonete
- Abdominal oblíquo solo (3x20 cada lado) - Peso corporal

### Quinta-feira (Ombros e Trapézio)
- Desenvolvimento militar ({}x{}) - Barra ou Halteres
- Elevação lateral ({}x{}) - Halteres
- Elevação frontal ({}x{}) - Halteres
- Encolhimento de ombros ({}x{}) - Barra
- Desenvolvimento Arnold ({}x{}) - Halteres
- Crucifixo inverso máquina ({}x{}) - Máquina de deltoide posterior

### Sexta-feira (Glúteos e Abdômen)
""".format(
        series, reps, series, reps, series, reps, series, reps, series, reps, series, reps,  # Segunda
        series, reps, series, reps, series, reps, series, reps, series, reps, series, reps,  # Terça
        series, reps, series, reps, series, reps, series, reps, series, reps, series, reps,  # Quarta (pernas)
        series, reps, series, reps, series, reps,  # Quinta (ombros)
        series, reps, series, reps, series, reps  # Quinta continuação
    )

    # Sexta-feira foco Glúteo + Abdômen
    if genero == "feminino":
        treino += f"""
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
        treino += f"""
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

    treino += "\n---\n"
    treino += "_Recomendamos avaliação médica antes de iniciar atividades físicas._\n"

    treino += f"\n**Observação:** Este treino foi adaptado para **{genero.capitalize()} {experiencia.capitalize()}** visando **{objetivo.capitalize()}**.\n"

    return treino

# Exibir treino
def exibir_treino(usuario):
    treino = gerar_treino(usuario)
    st.markdown(treino)
