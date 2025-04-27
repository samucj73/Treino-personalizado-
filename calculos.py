# Função para calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para calcular TMB
def calcular_tmb(idade, peso, altura, genero):
    if genero == "masculino":
        tmb = 10 * peso + 6.25 * altura * 100 - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura * 100 - 5 * idade - 161
    return tmb
