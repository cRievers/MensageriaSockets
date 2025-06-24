import tkinter as tk

def mostrar_mensagem():
    label.config(text="Mensagem exibida!")

# Cria a janela principal
janela = tk.Tk()
janela.title("Exemplo com Label")

# Cria um rótulo (label)
label = tk.Label(janela, text="Clique no botão para ver uma mensagem.")
label.pack()

# Cria um botão que chama a função mostrar_mensagem ao ser clicado
botao = tk.Button(janela, text="Mostrar Mensagem", command=mostrar_mensagem)
botao.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()