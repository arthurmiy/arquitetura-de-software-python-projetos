import document as model

view = None

def atribuir_view(_view):
    global view
    view = _view

# Função para adicionar atendente
def adicionar_atendente(nome):
    resultado = model.adicionar_atendente(nome)
    if resultado == "vazio":
        view.alerta("Nome vazio", "Digite um nome!")
    elif resultado == "duplicado":
        view.alerta("Duplicado", "Atendente já existe.")
    elif resultado == "ok":
        view.atualizar_interface()

# Função para resetar os dados de todas as pessoas atendentes
def resetar_atendentes():
    model.resetar()
    view.atualizar_interface()

def incrementar_vendas(indice):
    model.incrementar_vendas(indice)
    view.atualizar_interface()

def lista_atendentes():
    return model.obter_atendentes()