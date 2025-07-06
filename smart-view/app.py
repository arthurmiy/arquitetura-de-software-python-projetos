import tkinter as tk
from tkinter import messagebox

# Lista com os dados das pessoas atendentes
atendentes = []

# Função para adicionar atendente
def adicionar_atendente():
    nome = entrada_nome.get().strip()
    
    if not nome:
        messagebox.showwarning("Nome vazio", "Digite um nome!")
        return
    
    if nome in [a["nome"] for a in atendentes]:
        messagebox.showinfo("Duplicado", "Atendente já existe.")
        return

    atendentes.append({"nome": nome, "vendas": 0})
    entrada_nome.delete(0, tk.END)

# Função para resetar os dados de todas as pessoas atendentes
def resetar_atendentes():
    if messagebox.askyesno("Resetar", "Tem certeza que deseja resetar todos os dados?"):
        atendentes.clear()

# Função para incrementar as vendas de atendente
def incrementar_vendas(indice):
    atendentes[indice]["vendas"] += 1

# Função que desenha atendentes na interface
def atualizar_interface():
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()

    for i, atendente in enumerate(atendentes):
        texto = f"{atendente['nome']}: {atendente['vendas']} vendas"
        rotulo = tk.Label(quadro_atendentes, text=texto)
        rotulo.grid(row=i, column=0, sticky="w")

        botao_incrementar = tk.Button(
            quadro_atendentes, 
            text="+1", 
            command=lambda indice=i: incrementar_vendas(indice)
        )
        botao_incrementar.grid(row=i, column=1)

# Interface principal
janela = tk.Tk()
janela.title("Controle de Vendas – Smart View")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

botao_adicionar = tk.Button(janela, text="Adicionar Atendente", command=adicionar_atendente)
botao_adicionar.pack()

botao_resetar = tk.Button(janela, text="Resetar", command=resetar_atendentes)
botao_resetar.pack()

quadro_atendentes = tk.Frame(janela)
quadro_atendentes.pack(pady=10)

janela.mainloop()