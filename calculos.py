import streamlit as st

# Função para calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        faixa_imc = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        faixa_imc = "Peso normal"
    elif 25 <= imc < 29.9:
        faixa_imc = "Sobrepeso"
    else:
        faixa_imc = "Obesidade"
    return imc, faixa_imc

# Função para calcular TMB
def calcular_tmb(idade, peso, altura, genero):
    if genero == "Masculino":
        tmb = 10 * peso + 6.25 * altura * 100 - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura * 100 - 5 * idade - 161
    return tmb

# Função para calcular calorias diárias
def calcular_calorias_diarias(tmb, nivel_atividade):
    fatores = {
        "Sedentário": 1.2,
        "Leve": 1.375,
        "Moderado": 1.55,
        "Intenso": 1.725,
        "Muito intenso": 1.9
    }
    return tmb * fatores.get(nivel_atividade, 1.2)

# Função para calcular percentual de gordura
def calcular_percentual_gordura(peso, circunferencia_cintura, idade, genero):
    if genero == "Masculino":
        gordura = (0.1 * peso) + (0.23 * circunferencia_cintura) - (0.25 * idade) - 5.4
    else:
        gordura = (0.1 * peso) + (0.23 * circunferencia_cintura) - (0.25 * idade) - 4.5
    return gordura

# Função para calcular massa muscular
def calcular_massa_muscular(peso, percentual_gordura):
    return peso * (1 - percentual_gordura / 100)

# Função para calcular gasto calórico de exercício
def calcular_gasto_calorico_exercicio(tipo_exercicio, duracao):
    gasto_exercicio = {
        "Caminhada": 280,
        "Corrida": 600,
        "Natação": 700,
        "Musculação": 400,
        "Bicicleta": 500
    }
    return gasto_exercicio.get(tipo_exercicio, 0) * (duracao / 60)

# Função para calcular idade metabólica
def calcular_idade_metabolica(tmb, idade):
    return idade + (tmb - 1500) / 25

# Função para recomendação de água
def recomendacao_hidratacao(peso):
    return peso * 35  # ml por kg

# Função para recomendação de proteína
def recomendacao_proteina(peso, objetivo):
    if objetivo == "Aumento muscular":
        proteina = peso * 2.0
    elif objetivo == "Manutenção":
        proteina = peso * 1.5
    else:  # Emagrecimento
        proteina = peso * 1.2
    return proteina

# Interface do App
st.title("Calculadora de Saúde e Performance")

st.header("Informe seus dados:")

# Layout usando colunas
col1, col2 = st.columns(2)

with col1:
    peso = st.number_input("Peso (kg)", value=75.0, step=0.1)
    altura = st.number_input("Altura (m)", value=1.75, step=0.01)
    idade = st.number_input("Idade", value=30, step=1)
    circunferencia_cintura = st.number_input("Circunferência da Cintura (cm)", value=85.0, step=0.1)

with col2:
    genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
    nivel_atividade = st.selectbox("Nível de Atividade Física", ["Sedentário", "Leve", "Moderado", "Intenso", "Muito intenso"])
    tipo_exercicio = st.selectbox("Tipo de Exercício", ["Caminhada", "Corrida", "Natação", "Musculação", "Bicicleta"])
    duracao_exercicio = st.slider("Duração do Exercício (minutos)", 10, 120, 45)
    objetivo = st.selectbox("Objetivo", ["Aumento muscular", "Manutenção", "Emagrecimento"])

if st.button("Calcular"):
    # Calcular todos os resultados
    imc, faixa_imc = calcular_imc(peso, altura)
    tmb = calcular_tmb(idade, peso, altura, genero)
    calorias = calcular_calorias_diarias(tmb, nivel_atividade)
    percentual_gordura = calcular_percentual_gordura(peso, circunferencia_cintura, idade, genero)
    massa_muscular = calcular_massa_muscular(peso, percentual_gordura)
    gasto_exercicio = calcular_gasto_calorico_exercicio(tipo_exercicio, duracao_exercicio)
    idade_metabolica = calcular_idade_metabolica(tmb, idade)
    agua_necessaria = recomendacao_hidratacao(peso)
    proteina_necessaria = recomendacao_proteina(peso, objetivo)

    st.subheader("Resultados:")
    st.write(f"**IMC:** {imc:.2f} ({faixa_imc})")
    st.write(f"**TMB:** {tmb:.2f} kcal/dia")
    st.write(f"**Calorias Diárias Recomendadas:** {calorias:.2f} kcal")
    st.write(f"**Percentual de Gordura Corporal Estimado:** {percentual_gordura:.2f}%")
    st.write(f"**Massa Muscular Estimada:** {massa_muscular:.2f} kg")
    st.write(f"**Gasto Calórico no Exercício ({tipo_exercicio}):** {gasto_exercicio:.2f} kcal")
    st.write(f"**Idade Metabólica Estimada:** {idade_metabolica:.2f} anos")
    st.write(f"**Ingestão Recomendada de Água:** {agua_necessaria:.0f} ml/dia")
    st.write(f"**Ingestão Recomendada de Proteína:** {proteina_necessaria:.0f} g/dia")
