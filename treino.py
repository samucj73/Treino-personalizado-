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
        treino += """
**Treino A (Peito e Tríceps)**  
- Supino reto com halteres (3x15)  
- Crossover no cabo (3x20)  
- Tríceps corda (3x20)  

**Treino B (Costas e Bíceps)**  
- Puxada frente aberta (3x15)  
- Remada baixa (3x15)  
- Rosca direta (3x20)  

**Treino C (Pernas e Abdômen)**  
- Agachamento livre (3x15)  
- Leg press (3x20)  
- Abdominal prancha (3x30s)  

**Treino D (Ombros)**  
- Desenvolvimento com halteres (3x15)  
- Elevação lateral (3x20)  

**Treino E (Cardio/Funcional)**  
- Corrida/caminhada (30 minutos)  
- Circuito funcional (20 minutos)  
"""
    elif objetivo == "hipertrofia":
        treino += """
**Treino A (Peito e Tríceps)**  
- Supino reto barra (4x8)  
- Supino inclinado halteres (4x10)  
- Tríceps francês (4x12)  

**Treino B (Costas e Bíceps)**  
- Barra fixa assistida (4x8)  
- Remada unilateral (4x10)  
- Rosca alternada (4x12)  

**Treino C (Pernas e Abdômen)**  
- Agachamento livre (4x8)  
- Leg press (4x10)  
- Stiff (4x10)  
- Abdominal infra solo (3x20)  

**Treino D (Ombro e Trapézio)**  
- Desenvolvimento militar (4x8)  
- Elevação frontal (4x10)  
- Encolhimento trapézio (4x12)  

**Treino E (Cardio leve)**  
- Bicicleta ergométrica (20 minutos)  
"""
    else:  # resistência
        treino += """
**Treino A (Peito e Tríceps)**  
- Supino máquina (3x20)  
- Crossover leve (3x20)  
- Tríceps pulley (3x25)  

**Treino B (Costas e Bíceps)**  
- Puxada frente leve (3x20)  
- Remada máquina (3x20)  
- Rosca martelo (3x25)  

**Treino C (Pernas e Abdômen)**  
- Cadeira extensora (3x20)  
- Mesa flexora (3x20)  
- Abdominal oblíquo (3x30)  

**Treino D (Ombro e Core)**  
- Elevação lateral leve (3x20)  
- Prancha isométrica (3x30s)  

**Treino E (Cardio longo)**  
- Caminhada intensa (40 minutos)  
"""

    treino += "\n---\n"
    treino += "_Recomendamos avaliação médica antes de iniciar atividades físicas._"

    return treino

# Exibir treino
def exibir_treino(usuario):
    treino = gerar_treino(usuario)
    st.markdown(treino)
