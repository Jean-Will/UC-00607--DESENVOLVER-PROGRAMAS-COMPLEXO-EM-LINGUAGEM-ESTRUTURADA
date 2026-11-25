
from tkinter import *
from tkinter.ttk import Treeview
from ligacao import conectar

win = Tk()
win.title("Gestão da Base de Dados")
win.geometry("800x500")

# 1. Frame para os botoes
frameBotoes = Frame(win)
frameBotoes.pack(fill="x", padx=10, pady=10)

# 2. Criar a Treeview
tree = Treeview(win, show="headings")
tree.pack(fill="both", expand=True, padx=10, pady=10)


# 3. Funcao para limpar e preencher a tabela
def mostrarDados(sql, colunas):

    # Limpar dados anteriores
    tree.delete(*tree.get_children())

    # Configurar colunas
    tree["columns"] = colunas

    for coluna in colunas:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, width=150)

    # Ligacao a base de dados
    con = conectar()

    if not con:
        print("Erro na ligacao a base de dados")
        return

    cursor = con.cursor()

    try:
        cursor.execute(sql)
        resultados = cursor.fetchall()

        for linha in resultados:
            tree.insert("", "end", values=linha)

    except Exception as e:
        print("Erro:", e)

    finally:
        cursor.close()
        con.close()


# 4. Funcoes dos botoes

def mostrarFrutas():
    mostrarDados(
        "SELECT nome, precounit FROM produto",
        ("Fruta", "Preco")
    )


def mostrarProdutos():
    mostrarDados(
        "SELECT * FROM produto",
        ("ID", "Nome", "Preco")
    )


def mostrarClientes():
    mostrarDados(
        "SELECT * FROM cliente",
        ("ID", "Nome", "Email")
    )

def mostrarVendas():
    mostrarDados(
        """
        SELECT
            vender.cod,
            vender.pvenda,
            vender.codprod,
            cliente.nome
        FROM vender
        INNER JOIN cliente
            ON vender.codcl = cliente.cod
        """,
        ("Código", "Preço Venda", "Código Produto", "Cliente")
    )


# 5.  botoes

btnFrutas = Button(
    frameBotoes,
    text="Frutas",
    command=mostrarFrutas
)
btnFrutas.pack(side="left", padx=5)

btnProdutos = Button(
    frameBotoes,
    text="Produtos",
    command=mostrarProdutos
)
btnProdutos.pack(side="left", padx=5)

btnClientes = Button(
    frameBotoes,
    text="Clientes",
    command=mostrarClientes
)
btnClientes.pack(side="left", padx=5)

btnVendas = Button(
    frameBotoes,
    text="Vendas",
    command=mostrarVendas
)
btnVendas.pack(side="left", padx=5)

btnSair = Button(
    frameBotoes,
    text="Sair",
    command=exit
)
btnSair.pack(side="left", padx=5)


# 6. Iniciar a aplicacao
win.mainloop()
