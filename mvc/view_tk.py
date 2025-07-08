import tkinter as tk
from tkinter import messagebox
import controller

def alerta(titulo, msg):
    messagebox.showinfo(titulo, msg)

# Função que desenha atendentes na interface
def atualizar_interface():
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()

    for i, atendente in enumerate(controller.lista_atendentes()):
        rotulo = tk.Label(quadro_atendentes, text=f"{atendente['nome']}: {atendente['vendas']} vendas")
        rotulo.grid(row=i, column=0, sticky="w")

        botao_incrementar = tk.Button(
            quadro_atendentes, text="+1",
            command=lambda indice=i: [controller.incrementar_vendas(indice)]
        )
        botao_incrementar.grid(row=i, column=1)

# Interface principal
janela = tk.Tk()
janela.title("Controle de Vendas – Smart View")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

botao_adicionar = tk.Button(janela, text="Adicionar Atendente", command=lambda: [controller.adicionar_atendente(entrada_nome.get().strip()),entrada_nome.delete(0, tk.END)])
botao_adicionar.pack()

botao_resetar = tk.Button(janela, text="Resetar", command=controller.resetar_atendentes)
botao_resetar.pack()

quadro_atendentes = tk.Frame(janela)
quadro_atendentes.pack(pady=10)