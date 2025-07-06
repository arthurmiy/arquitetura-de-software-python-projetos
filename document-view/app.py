import tkinter as tk
from tkinter import messagebox
import document

# Função para adicionar atendente
def adicionar_atendente():
    nome = entrada_nome.get().strip()
    resultado = document.adicionar_atendente(nome)
    if resultado == "vazio":
        messagebox.showwarning("Nome vazio", "Digite um nome!")
    elif resultado == "duplicado":
        messagebox.showinfo("Duplicado", "Atendente já existe.")
    entrada_nome.delete(0, tk.END)
    atualizar_interface()

# Função para resetar os dados de todas as pessoas atendentes
def resetar_atendentes():
    if messagebox.askyesno("Resetar", "Tem certeza que deseja resetar?"):
        document.resetar()
        atualizar_interface()


# Função que desenha atendentes na interface
def atualizar_interface():
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()

    for i, atendente in enumerate(document.atendentes):
        rotulo = tk.Label(quadro_atendentes, text=f"{atendente['nome']}: {atendente['vendas']} vendas")
        rotulo.grid(row=i, column=0, sticky="w")

        botao_incrementar = tk.Button(
            quadro_atendentes, text="+1",
            command=lambda indice=i: [document.incrementar_vendas(indice), atualizar_interface()]
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

atualizar_interface()
janela.mainloop()