import tkinter as tk
from tkinter import messagebox

# Lista para armazenar os produtos cadastrados
produtos = []

# Função para cadastrar um produto
def cadastrar_produto():
    nome = nome_entry.get()
    descricao = descricao_entry.get()
    valor = valor_entry.get()
    disponivel = disponivel_var.get()

    if not nome or not valor:
        messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios!")
        return

    try:
        valor_float = float(valor)
    except ValueError:
        messagebox.showwarning("Atenção", "O valor deve ser numérico!")
        return

    # Adicionar produto à lista
    produto = {
        "nome": nome,
        "descricao": descricao,
        "valor": valor_float,
        "disponivel": disponivel
    }
    produtos.append(produto)

    # Limpar os campos após o cadastro
    nome_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)

    listar_produtos()  # Atualizar a listagem automaticamente

# Função para listar os produtos cadastrados
def listar_produtos():
    # Ordenar os produtos pelo valor, do menor para o maior
    produtos_ordenados = sorted(produtos, key=lambda p: p["valor"])

    # Limpar a tabela antes de atualizá-la
    for widget in listagem_frame.winfo_children():
        widget.destroy()

    # Adicionar cabeçalhos à tabela
    tk.Label(listagem_frame, text="Nome", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(listagem_frame, text="Valor (R$)", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

    # Adicionar os produtos à listagem
    for i, produto in enumerate(produtos_ordenados):
        tk.Label(listagem_frame, text=produto["nome"]).grid(row=i+1, column=0, padx=10, pady=5)
        tk.Label(listagem_frame, text=f'{produto["valor"]:.2f}').grid(row=i+1, column=1, padx=10, pady=5)

    # Botão para cadastrar um novo produto a partir da listagem
    btn_cadastrar_novo = tk.Button(listagem_frame, text="Cadastrar Novo Produto", command=abrir_formulario)
    btn_cadastrar_novo.grid(row=len(produtos_ordenados) + 1, columnspan=2, pady=10)

# Função para abrir o formulário de cadastro de produtos
def abrir_formulario():
    global nome_entry, descricao_entry, valor_entry, disponivel_sim, disponivel_nao, cadastrar_button, disponivel_var

    # Limpar o frame da listagem
    for widget in listagem_frame.winfo_children():
        widget.destroy()

    # Recriar os campos do formulário
    nome_entry = tk.Entry(listagem_frame)
    descricao_entry = tk.Entry(listagem_frame)
    valor_entry = tk.Entry(listagem_frame)

    # Campo de seleção Sim/Não para Disponível para Venda
    disponivel_var = tk.StringVar(value="Sim")
    disponivel_sim = tk.Radiobutton(listagem_frame, text="Sim", variable=disponivel_var, value="Sim")
    disponivel_nao = tk.Radiobutton(listagem_frame, text="Não", variable=disponivel_var, value="Não")

    # Exibir o formulário de cadastro
    tk.Label(listagem_frame, text="Nome do Produto:").grid(row=0, column=0, padx=10, pady=5)
    nome_entry.grid(row=0, column=1)

    tk.Label(listagem_frame, text="Descrição do Produto:").grid(row=1, column=0, padx=10, pady=5)
    descricao_entry.grid(row=1, column=1)

    tk.Label(listagem_frame, text="Valor do Produto (R$):").grid(row=2, column=0, padx=10, pady=5)
    valor_entry.grid(row=2, column=1)

    tk.Label(listagem_frame, text="Disponível para Venda:").grid(row=3, column=0, padx=10, pady=5)
    disponivel_sim.grid(row=3, column=1, sticky=tk.W)
    disponivel_nao.grid(row=3, column=1, sticky=tk.E)

    # Botão para cadastrar produto
    cadastrar_button = tk.Button(listagem_frame, text="Cadastrar Produto", command=cadastrar_produto)
    cadastrar_button.grid(row=4, columnspan=2, pady=10)

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("400x300")

# Criar o frame para a listagem/formulário
listagem_frame = tk.Frame(root)
listagem_frame.pack(pady=20)

# Exibir o formulário inicial
abrir_formulario()

# Iniciar o loop principal da interface
root.mainloop()

