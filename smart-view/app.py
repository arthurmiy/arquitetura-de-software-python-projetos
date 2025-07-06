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

# Interface principal
janela = tk.Tk()
janela.title("Controle de Vendas – Smart View")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

janela.mainloop()