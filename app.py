import streamlit as st
from usuario import cadastrar, obter
from treino import gerar_treino
from calculos import (
    calcular_imc,
    calcular_tmb,
    calcular_percentual_gordura,
    calcular_massa_muscular,
    calcular_idade_metabolica,
    recomendacao_hidratacao,
    recomendacao_proteina
)

# Função para exibir o treino
def exibir_treino(usuario):
    treino = gerar_treino(usuario)
    st.markdown(treino)

    # Calcular IMC e TMB
    imc, faixa_imc = calcular_imc(usuario[4], usuario[5])
    tmb = calcular_tmb(usuario[3], usuario[4], usuario[5], usuario[6])

    st.subheader("Cálculos de Saúde")
    st.write(f"**IMC (Índice de Massa Corporal):** {imc:.2f} ({faixa_imc})")
    st.write(f"**Taxa de Metabolismo Basal (TMB):** {tmb:.2f} kcal/dia")

    # Mostrar análises avançadas
    if st.button("Mostrar Análises Avançadas"):
        circunferencia_cintura = st.number_input("Circunferência da Cintura (cm)", min_value=50.0, max_value=200.0)

        percentual_gordura = calcular_percentual_gordura(usuario[4], circunferencia_cintura, usuario[3], usuario[6])
        massa_muscular = calcular_massa_muscular(usuario[4], percentual_gordura)
        idade_metabolica = calcular_idade_metabolica(tmb, usuario[3])
        agua_necessaria = recomendacao_hidratacao(usuario[4])
        proteina_necessaria = recomendacao_proteina(usuario[4], usuario[7])

        st.write(f"**Percentual de Gordura Estimado:** {percentual_gordura:.2f}%")
        st.write(f"**Massa Muscular Estimada:** {massa_muscular:.2f} kg")
        st.write(f"**Idade Metabólica Estimada:** {idade_metabolica:.1f} anos")
        st.write(f"**Ingestão Recomendada de Água:** {agua_necessaria:.0f} ml/dia")
        st.write(f"**Ingestão Recomendada de Proteína:** {proteina_necessaria:.0f} g/dia")

    if st.button("Exportar treino para PDF (em breve)"):
        st.info("Função de exportação em PDF ainda não implementada.")

# Interface de login
def login():
    st.subheader("Login")
    nome = st.text_input("Nome")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        usuario = obter(nome, senha)
        if usuario:
            st.session_state['usuario'] = usuario
            st.success(f"Bem-vindo(a), {usuario[1]}!")
            st.rerun()
        else:
            st.error("Nome ou senha inválidos!")

# Interface de cadastro
def cadastro():
    st.subheader("Cadastro")
    nome = st.text_input("Nome", key="cad_nome")
    senha = st.text_input("Senha", type="password", key="cad_senha")
    idade = st.number_input("Idade", min_value=18, max_value=120, key="cad_idade")
    peso = st.number_input("Peso (kg)", min_value=1.0, key="cad_peso")
    altura = st.number_input("Altura (m)", min_value=1.0, key="cad_altura")
    genero = st.selectbox("Gênero", ["masculino", "feminino"], key="cad_genero")
    objetivo = st.text_input("Objetivo", key="cad_objetivo")
    experiencia = st.selectbox("Experiência", ["iniciante", "intermediário", "avançado"], key="cad_experiencia")

    if st.button("Cadastrar"):
        cadastrar(nome, senha, idade, peso, altura, genero, objetivo, experiencia)
        st.success(f"Usuário {nome} cadastrado com sucesso!")
        st.info("Agora faça login para acessar seu treino.")

# Função principal
def main():
    st.title("🏋️‍♂️ App de Treino Personalizado")

    menu = st.sidebar.selectbox("Menu", ["Login", "Cadastro"])

    if 'usuario' in st.session_state:
        st.sidebar.success(f"Logado como: {st.session_state['usuario'][1]}")
        if st.sidebar.button("Sair"):
            del st.session_state['usuario']
            st.rerun()

        st.subheader("Seu Treino Personalizado")
        exibir_treino(st.session_state['usuario'])

    else:
        if menu == "Login":
            login()
        elif menu == "Cadastro":
            cadastro()

if __name__ == "__main__":
    main()
