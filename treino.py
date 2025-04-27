# Função para gerar treino
def gerar_treino(usuario):
    idade = usuario[3]
    peso = usuario[4]
    altura = usuario[5]
    genero = usuario[6]
    objetivo = usuario[7].lower()
    experiencia = usuario[8]

    treino = f"## Dados Físicos\n"
    treino += f"- **Idade:** {idade} anos\n"
    treino += f"- **Peso:** {peso:.1f} kg\n"
    treino += f"- **Altura:** {altura:.2f} m\n"
    treino += f"- **Objetivo:** {objetivo.capitalize()}\n"
    treino += "---\n\n"

    treino += "## Treino Semanal\n"

    if objetivo == "emagrecimento":
        cardio = "**Treino E (Cardio/Funcional)**\n- Corrida moderada (40 minutos)\n- Circuito funcional (30 minutos)\n"
        series_reps = "(3x20)"
    elif objetivo == "hipertrofia":
        cardio = "**Treino E (Cardio leve)**\n- Bicicleta ergométrica (20 minutos)\n- Caminhada leve (20 minutos)\n"
        series_reps = "(4x8-12)"
    else:  # resistência
        cardio = "**Treino E (Cardio longo)**\n- Caminhada intensa (45 minutos)\n- Corrida leve (30 minutos)\n"
        series_reps = "(3x20-25)"

    # Treino A: Peito e Tríceps
    treino += """
**Treino A (Peito e Tríceps)**

**Peito:**
- Supino reto com barra - Máquina/Banco {}
- Supino inclinado com halteres - Halteres/Banco {}
- Crossover no cabo - Crossover/Cabo {}
- Crucifixo reto com halteres - Halteres/Banco {}
- Flexão de braços no solo - Peso corporal {}
- Supino declinado com barra - Máquina/Banco {}

**Tríceps:**
- Tríceps testa com barra EZ - Barra/Anilha {}
- Tríceps pulley com corda - Cabo {}
- Tríceps francês unilateral - Halteres {}
- Tríceps mergulho em banco - Peso corporal {}
- Tríceps coice com halteres - Halteres {}
- Tríceps banco máquina - Máquina {}
""".format(series_reps, series_reps, series_reps, series_reps, series_reps, series_reps,
           series_reps, series_reps, series_reps, series_reps, series_reps, series_reps)

    # Treino B: Costas e Bíceps
    treino += """
**Treino B (Costas e Bíceps)**

**Costas:**
- Puxada frente aberta - Máquina/Cabo {}
- Remada curvada com barra - Barra {}
- Remada baixa - Máquina/Cabo {}
- Remada unilateral com halteres - Halteres {}
- Puxada neutra (pegada fechada) - Máquina/Cabo {}
- Pullover na máquina - Máquina {}

**Bíceps:**
- Rosca direta barra EZ - Barra {}
- Rosca alternada - Halteres {}
- Rosca concentrada - Halteres {}
- Rosca martelo - Halteres {}
- Rosca scott máquina - Máquina {}
- Rosca inversa com barra - Barra {}
""".format(series_reps, series_reps, series_reps, series_reps, series_reps, series_reps,
           series_reps, series_reps, series_reps, series_reps, series_reps, series_reps)

    # Treino C: Pernas + Abdômen
    treino += """
**Treino C (Pernas e Abdômen)**

**Pernas (Quadríceps, Posterior, Glúteo):**
- Agachamento livre - Barra {}
- Leg press 45° - Máquina {}
- Cadeira extensora - Máquina {}
- Mesa flexora - Máquina {}
- Stiff com halteres - Halteres {}
- Avanço (passada) com halteres - Halteres {}

**Abdômen:**
- Prancha isométrica - Peso corporal (3x30s)
- Abdominal supra solo - Peso corporal (3x30)
- Abdominal oblíquo com halteres - Halteres (3x20)
""".format(series_reps, series_reps, series_reps, series_reps, series_reps, series_reps)

    # Treino D: Ombro e Trapézio
    treino += """
**Treino D (Ombro e Trapézio)**

**Ombro:**
- Desenvolvimento militar com barra - Barra {}
- Desenvolvimento com halteres - Halteres {}
- Elevação lateral com halteres - Halteres {}
- Elevação frontal com halteres - Halteres {}
- Crucifixo inverso no peck deck - Máquina {}
- Remada alta com barra - Barra {}

**Trapézio:**
- Encolhimento de ombros com halteres - Halteres {}
- Encolhimento com barra - Barra {}
- Remada alta pegada fechada - Barra {}
- Trapézio máquina - Máquina {}
- Remada alta no cross-over - Cabo {}
- Shrug no smith - Máquina Smith {}
""".format(series_reps, series_reps, series_reps, series_reps, series_reps, series_reps,
           series_reps, series_reps, series_reps, series_reps, series_reps, series_reps)

    treino += "\n" + cardio
    treino += "\n---\n"
    treino += "_Recomendamos avaliação médica antes de iniciar atividades físicas._"

    return treino

# Exibir treino
def exibir_treino(usuario):
    treino = gerar_treino(usuario)
    st.markdown(treino)
