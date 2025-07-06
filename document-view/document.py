#document.py - Não depende do tkinter

# Lista com os dados das pessoas atendentes
atendentes = []

# Função para adicionar atendente
def adicionar_atendente(nome):
    if not nome:
        return "vazio"
    if nome in [a["nome"] for a in atendentes]:
        return "duplicado"
    atendentes.append({"nome": nome, "vendas": 0})
    return "ok"

# Função para resetar os dados de todas as pessoas atendentes
def resetar():
    atendentes.clear()

# Função para incrementar as vendas de atendente
def incrementar_vendas(indice):
    atendentes[indice]["vendas"] += 1

def obter_atendentes():
    return atendentes