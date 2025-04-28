import streamlit as st  # Adiciona a importação do streamlit
# Função para calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    faixa_imc = ""
    if imc < 18.5:
        faixa_imc = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        faixa_imc = "Peso normal"
    elif 25 <= imc < 29.9:
        faixa_imc = "Sobrepeso"
    else:
        faixa_imc = "Obesidade"
    return imc, faixa_imc

# Função para calcular TMB (Taxa de Metabolismo Basal)
def calcular_tmb(idade, peso, altura, genero):
    if genero == "masculino":
        tmb = 10 * peso + 6.25 * altura * 100 - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura * 100 - 5 * idade - 161
    return tmb

# Função para calcular calorias diárias com base no nível de atividade física
def calcular_calorias_diarias(tmb, nivel_atividade):
    if nivel_atividade == "sedentario":
        calorias = tmb * 1.2
    elif nivel_atividade == "leve":
        calorias = tmb * 1.375
    elif nivel_atividade == "moderado":
        calorias = tmb * 1.55
    elif nivel_atividade == "intenso":
        calorias = tmb * 1.725
    else:  # Nível de atividade muito intenso
        calorias = tmb * 1.9
    return calorias

# Função para estimar o percentual de gordura corporal
def calcular_percentual_gordura(peso, circunferencia_cintura, idade, genero):
    if genero == "masculino":
        gordura = (0.1 * peso) + (0.23 * circunferencia_cintura) - (0.25 * idade) - 5.4
    else:  # Gênero feminino
        gordura = (0.1 * peso) + (0.23 * circunferencia_cintura) - (0.25 * idade) - 4.5
    return gordura

# Função para estimar a massa muscular (porcentagem de massa magra)
def calcular_massa_muscular(peso, percentual_gordura):
    massa_magra = peso * (1 - (percentual_gordura / 100))
    return massa_magra

# Função para calcular gasto calórico com exercícios
def calcular_gasto_calorico_exercicio(tipo_exercicio, duracao):
    # Estimativas médias de gasto calórico por hora (para uma pessoa de 70kg)
    gasto_exercicio = {
        "caminhada": 280,
        "corrida": 600,
        "natação": 700,
        "musculação": 400,
        "bicicleta": 500
    }
    if tipo_exercicio in gasto_exercicio:
        gasto = gasto_exercicio[tipo_exercicio] * (duracao / 60)  # Duracao em minutos
    else:
        gasto = 0
    return gasto

# Função para calcular a idade metabólica (aproximada)
def calcular_idade_metabolica(tmb, idade):
    idade_metabolica = idade + (tmb - 1500) / 25
    return idade_metabolica

# Função para recomendação de ingestão de água
def recomendacao_hidratacao(peso):
    agua_necessaria = peso * 35  # ml por kg de peso
    return agua_necessaria

# Função para recomendar a ingestão de proteínas
def recomendacao_proteina(peso, objetivo):
    if objetivo == "aumento_muscular":
        proteina = peso * 2.0  # 2g por kg para ganho de massa muscular
    elif objetivo == "manutencao":
        proteina = peso * 1.5  # 1.5g por kg para manutenção
    else:  # Objetivo de emagrecimento
        proteina = peso * 1.2  # 1.2g por kg para emagrecimento
    return proteina

# Exemplo de uso:
peso = 75  # em kg
altura = 1.75  # em metros
idade = 30
genero = "masculino"
nivel_atividade = "moderado"
circunferencia_cintura = 85  # em cm
tipo_exercicio = "corrida"  # Exemplo de exercício
duracao_exercicio = 45  # Em minutos
objetivo = "aumento_muscular"  # Exemplo de objetivo

# Calcular IMC
imc, faixa_imc = calcular_imc(peso, altura)
st.write(f"**IMC (Índice de Massa Corporal):** {imc:.2f} ({faixa_imc})")

# Calcular TMB
tmb = calcular_tmb(idade, peso, altura, genero)
st.write(f"TMB: {tmb:.2f} kcal/dia")

# Calcular calorias diárias
calorias = calcular_calorias_diarias(tmb, nivel_atividade)
st.write(f"Calorias necessárias: {calorias:.2f} kcal/dia")

# Calcular percentual de gordura corporal
percentual_gordura = calcular_percentual_gordura(peso, circunferencia_cintura, idade, genero)
st.write(f"Percentual de gordura corporal estimado: {percentual_gordura:.2f}%")

# Calcular massa muscular
massa_muscular = calcular_massa_muscular(peso, percentual_gordura)
st.write(f"Massa muscular estimada: {massa_muscular:.2f} kg")

# Calcular gasto calórico com exercício
gasto_exercicio = calcular_gasto_calorico_exercicio(tipo_exercicio, duracao_exercicio)
st.write(f"Gasto calórico com {tipo_exercicio}: {gasto_exercicio:.2f} kcal")

# Calcular idade metabólica
idade_metabolica = calcular_idade_metabolica(tmb, idade)
st.write(f"Idade metabólica estimada: {idade_metabolica:.2f} anos")

# Recomendação de ingestão de água
agua_necessaria = recomendacao_hidratacao(peso)
st.write(f"Ingestão recomendada de água: {agua_necessaria:.2f} ml/dia")

# Recomendar ingestão de proteína
proteina_necessaria = recomendacao_proteina(peso, objetivo)
st.write(f"Ingestão recomendada de proteína: {proteina_necessaria:.2f} g/dia")
