import tkinter as tk
from tkinter import messagebox

import requests


def buscar_endereco():
    cep = entrada_cep.get() #Obtém o valor digitado pelo usuário
    if not cep.isdigit() or len(cep) !=8: #Valida o CEP
        messagebox.showerror("Erro", "Por favor, insira um CEP válido (8 numeros).")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json() #Converte a resposta para JSON

        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
        else:
            resultado.set(f"Endereço: {dados['logradouro']}\n"
                          f"Bairro: {dados['bairro']}\n"
                          f"Cidade: {dados['localidade']}\n"
                          f"Estado: {dados['uf']}")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Erro ao acessar a API: {e}")



# Criando interface gráfica
app = tk.Tk()
app.title("Buscar Endereço pelo CEP")

tk.Label(app, text="Digite o Cep: ").pack(pady=5)
entrada_cep = tk.Entry(app, width=20)
entrada_cep.pack(pady=5)

tk.Button(app, text="Buscar", command= buscar_endereco).pack(pady=5)
resultado = tk.StringVar()
tk.Label(app, textvariable=resultado, justify="left").pack(pady=10)

app.mainloop()