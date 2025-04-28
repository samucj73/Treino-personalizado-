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

    idade = usuario[3]
    peso = usuario[4]
    altura = usuario[5]
    genero = usuario[6]
    objetivo = usuario[7]

    circunferencia_cintura = 85  # Valor fixo temporário

    st.subheader("Resumo de Saúde")

    col1, col2 = st.columns(2)

    with col1:
        imc, faixa_imc = calcular_imc(peso, altura)
        st.metric("IMC", f"{imc:.2f}", faixa_imc)

    with col2:
        tmb = calcular_tmb(idade, peso, altura, genero)
        st.metric("TMB", f"{tmb:.0f} kcal/dia")

    with st.expander("Análise Avançada de Saúde e Recomendações"):
        percentual_gordura = calcular_percentual_gordura(peso, circunferencia_cintura, idade, genero)
        massa_muscular = calcular_massa_muscular(peso, percentual_gordura)
        idade_metabolica = calcular_idade_metabolica(tmb, idade)
        agua_necessaria = recomendacao_hidratacao(peso)
        proteina_necessaria = recomendacao_proteina(peso, objetivo)

        st.write(f"**Percentual de Gordura Corporal Estimado:** {percentual_gordura:.2f}%")
        st.write(f"**Massa Muscular Estimada:** {massa_muscular:.2f} kg")
        st.write(f"**Idade Metabólica Estimada:** {idade_metabolica:.1f} anos")
        st.write(f"**Ingestão Recomendada de Água:** {agua_necessaria:.0f} ml/dia")
        st.write(f"**Ingestão Recomendada de Proteína:** {proteina_necessaria:.0f} g/dia")

    if st.button("Exportar treino para PDF (em breve)"):
        st.info("Função de exportação em PDF ainda não implementada.")

# Função para criar perfil rápido (se o usuário logar sem dados completos)
def preencher_dados_usuario():
    st.subheader("Complete seu Perfil de Treino")

    with st.form("formulario_usuario"):
        idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
        peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, step=0.1)
        altura = st.number_input("Altura (metros)", min_value=1.0, max_value=2.5, step=0.01)
        genero = st.selectbox("Gênero", ["masculino", "feminino"])
        objetivo = st.selectbox("Objetivo", ["hipertrofia", "emagrecimento", "resistência", "manutenção"])
        experiencia = st.selectbox("Nível de Experiência", ["iniciante", "intermediário", "avançado"])
        dias_treino = st.selectbox("Quantos dias por semana pode treinar?", [2, 3, 4, 5])

        submitted = st.form_submit_button("Salvar Perfil")

    if submitted:
        usuario_atual = list(st.session_state['usuario'])
        usuario_atual[3] = idade
        usuario_atual[4] = peso
        usuario_atual[5] = altura
        usuario_atual[6] = genero
        usuario_atual[7] = objetivo
        usuario_atual.append(experiencia)
        usuario_atual.append(dias_treino)

        st.session_state['usuario'] = usuario_atual
        st.success("Perfil atualizado! Agora seu treino será gerado corretamente.")
        st.rerun()

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
    st.set_page_config(page_title="Gerador de Treino Personalizado", layout="wide")
    st.title("🏋️‍♂️ App de Treino Personalizado")

    menu = st.sidebar.selectbox("Menu", ["Login", "Cadastro"])

    if 'usuario' in st.session_state:
        st.sidebar.success(f"Logado como: {st.session_state['usuario'][1]}")
        if st.sidebar.button("Sair"):
            del st.session_state['usuario']
            st.rerun()

        usuario = st.session_state['usuario']

        # Se faltar dados, pedir para completar perfil
        if len(usuario) < 10:  
            preencher_dados_usuario()
        else:
            st.subheader("Seu Treino Personalizado")
            exibir_treino(usuario)

    else:
        if menu == "Login":
            login()
        elif menu == "Cadastro":
            cadastro()

if __name__ == "__main__":
    main()
