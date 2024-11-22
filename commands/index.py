from datetime import datetime
import tkinter as tk
import requests

# Função para definir e atualizar o horário
def atualizar_horario():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    label.config(text=agora)
    root.after(1000, atualizar_horario)

# Pegando as cotações da API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = float(cotacoes['USDBRL']["bid"])
cotacao_euro = float(cotacoes['EURBRL']["bid"])
cotacao_bitcoin = float(cotacoes['BTCBRL']["bid"])

cotacao_dolar_str = str(f"{cotacao_dolar:.2f}")
cotacao_euro_str = str(f"{cotacao_euro:.2f}")
cotacao_bitcoin_str = str(f"{cotacao_bitcoin:.2f}")

# Criando a janela principal
root = tk.Tk()
root.geometry("400x270")
root.config(bg="#363636")  
root.font = ("Courier New", 12, "bold")
root.title('Cotações de Moedas | 30 Segundos')

# Título da janela
tk.Label(root, text='Cotações Atualizadas', font=('Helvetica', 20, 'bold')).pack(pady=20)

# Exibir as cotações da API
tk.Label(
    root,
    text=f"Cotação do Dolar = {cotacao_dolar_str}",
    font=root.font,
    bg="lightgray",
    fg="black",
    relief="solid",
    bd=1,
    padx=10,
    pady=5
).pack(pady=10)

tk.Label(
    root,
    text=f"Cotação do Euro = {cotacao_euro_str}",
    font=root.font,
    bg="lightgray",
    fg="black",
    relief="solid",
    bd=1,
    padx=10,
    pady=5
).pack(pady=10)

tk.Label(
    root,
    text=f"Cotação do Bitcoin = {cotacao_bitcoin_str}",
    font=root.font,
    bg="lightgray",
    fg="black",
    relief="solid",
    bd=1,
    padx=10,
    pady=5
).pack(pady=10)

# Exibir o horário no canto inferior direito
label = tk.Label(root, font=("Courier New", 10, "bold"), fg="black", bg="lightgray")
label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Inicia a atualização do horário
atualizar_horario()

# Inicializa o programa
root.mainloop()