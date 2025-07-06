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