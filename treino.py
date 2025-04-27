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

    treino += "## Divisão Semanal\n"
    treino += """
- **Segunda-feira:** Treino A (Peito + Tríceps)
- **Terça-feira:** Treino B (Costas + Bíceps)
- **Quarta-feira:** Treino C (Pernas + Abdômen)
- **Quinta-feira:** Treino D (Ombro + Trapézio)
- **Sexta-feira:** Treino E (Cardio)
- **Sábado:** (Opcional) Repetir Treino A ou treino funcional/alongamento
- **Domingo:** Descanso
"""

    treino += "---\n\n"
    treino += "## Treino Detalhado\n"

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
    treino += f"""
**Treino A (Peito e Tríceps)**

**Peito:**
- Supino reto com barra - Máquina/Banco {series_reps}
- Supino inclinado com halteres - Halteres/Banco {series_reps}
- Crossover no cabo - Crossover/Cabo {series_reps}
- Crucifixo reto com halteres - Halteres/Banco {series_reps}
- Flexão de braços no solo - Peso corporal {series_reps}
- Supino declinado com barra - Máquina/Banco {series_reps}

**Tríceps:**
- Tríceps testa com barra EZ - Barra/Anilha {series_reps}
- Tríceps pulley com corda - Cabo {series_reps}
- Tríceps francês unilateral - Halteres {series_reps}
- Tríceps mergulho em banco - Peso corporal {series_reps}
- Tríceps coice com halteres - Halteres {series_reps}
- Tríceps banco máquina - Máquina {series_reps}
"""

    # Treino B: Costas e Bíceps
    treino += f"""
**Treino B (Costas e Bíceps)**

**Costas:**
- Puxada frente aberta - Máquina/Cabo {series_reps}
- Remada curvada com barra - Barra {series_reps}
- Remada baixa - Máquina/Cabo {series_reps}
- Remada unilateral com halteres - Halteres {series_reps}
- Puxada neutra (pegada fechada) - Máquina/Cabo {series_reps}
- Pullover na máquina - Máquina {series_reps}

**Bíceps:**
- Rosca direta barra EZ - Barra {series_reps}
- Rosca alternada - Halteres {series_reps}
- Rosca concentrada - Halteres {series_reps}
- Rosca martelo - Halteres {series_reps}
- Rosca scott máquina - Máquina {series_reps}
- Rosca inversa com barra - Barra {series_reps}
"""

    # Treino C: Pernas + Abdômen
    treino += f"""
**Treino C (Pernas e Abdômen)**

**Pernas (Quadríceps, Posterior, Glúteo):**
- Agachamento livre - Barra {series_reps}
- Leg press 45° - Máquina {series_reps}
- Cadeira extensora - Máquina {series_reps}
- Mesa flexora - Máquina {series_reps}
- Stiff com halteres - Halteres {series_reps}
- Avanço (passada) com halteres - Halteres {series_reps}

**Abdômen:**
- Prancha isométrica - Peso corporal (3x30s)
- Abdominal supra solo - Peso corporal (3x30)
- Abdominal oblíquo com halteres - Halteres (3x20)
"""

    # Treino D: Ombro e Trapézio
    treino += f"""
**Treino D (Ombro e Trapézio)**

**Ombro:**
- Desenvolvimento militar com barra - Barra {series_reps}
- Desenvolvimento com halteres - Halteres {series_reps}
- Elevação lateral com halteres - Halteres {series_reps}
- Elevação frontal com halteres - Halteres {series_reps}
- Crucifixo inverso no peck deck - Máquina {series_reps}
- Remada alta com barra - Barra {series_reps}

**Trapézio:**
- Encolhimento de ombros com halteres - Halteres {series_reps}
- Encolhimento com barra - Barra {series_reps}
- Remada alta pegada fechada - Barra {series_reps}
- Trapézio máquina - Máquina {series_reps}
- Remada alta no cross-over - Cabo {series_reps}
- Shrug no smith - Máquina Smith {series_reps}
"""

    treino += "\n" + cardio
    treino += "\n---\n"
    treino += "_Recomendamos avaliação médica antes de iniciar atividades físicas._"

    return treino

# Exibir treino
def exibir_treino(usuario):
    treino = gerar_treino(usuario)
    st.markdown(treino)
