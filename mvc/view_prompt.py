import controller
from types import SimpleNamespace

# ------------------------------------------------------------
# Funções que o Controller espera da View
# ------------------------------------------------------------

def atualizar_interface():
    """Exibe a lista de atendentes ordenada segundo o Model."""
    print("\n=== CONTADOR DE VENDAS ===")
    atendentes = controller.lista_atendentes()
    if not atendentes:
        print("(Sem atendentes)")
    else:
        for idx, a in enumerate(atendentes, start=1):
            print(f"{idx}. {a['nome']}: {a['vendas']} vendas")
    print("--------------------------\n")


def alerta(titulo: str, mensagem: str):
    """Mostra uma mensagem simples no console."""
    print(f"[{titulo}] {mensagem}\n")


# ------------------------------------------------------------
# Loop principal da CLI
# ------------------------------------------------------------

def loop_cli():
    """Loop de leitura de comandos do usuário."""
    atualizar_interface()
    print("Instruções:")
    print("  <nome>        → adiciona atendente")
    print("  <indice>+     → incrementa vendas (ex.: 2+)\n  q ou quit     → sair\n")

    while True:
        comando = input("> ").strip()
        if not comando:
            atualizar_interface()
            continue

        if comando.lower() in {"q", "quit", "sair"}:
            break

        # Incremento: formato N+
        if comando.endswith("+") and comando[:-1].isdigit():
            indice = int(comando[:-1]) - 1  # Conversão p/ índice 0‑based
            controller.incrementar_vendas(indice)
        else:
            # Tenta adicionar atendente com esse texto como nome
            controller.adicionar_atendente(comando)


# ------------------------------------------------------------
# Entry point
# ------------------------------------------------------------

if __name__ == "__main__":
    #  - Usamos um SimpleNamespace para expor atualizar() e alerta()
    view_ns = SimpleNamespace(atualizar_interface=atualizar_interface, alerta=alerta)
    controller.atribuir_view(view_ns)

    # Inicia o loop da CLI
    loop_cli()