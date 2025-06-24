import socket
import threading
import json
import tkinter as tk

def cadastro(numero, nome):
    if( ehValido(numero) and nome!= None):
        adicionarCtt(numero, nome)

def adicionarCtt(numero, nome):
    dados = {
        "numero": numero,
        "nome": nome
    }
    arquivo = open("cadastro.json", "w")
    json.dump(dados, arquivo)
    arquivo.close()




def handle_client(conexao, cliente):
    """
    Função para lidar com a conexão de um cliente em uma thread separada.
    """
    print(f"NOVA CONEXÃO: {cliente} se conectou.")
    try:
        while True:
            # Recebe dados do cliente (até 1024 bytes)
            data = conexao.recv(1024)
            # Se não receber dados, o cliente desconectou
            if not data:
                print(f"CLIENTE DESCONECTADO: {cliente}")
                break
            # Imprime os dados recebidos e os envia de volta (echo)
            print(f"Recebido de {cliente}: {data.decode('utf-8')}")
            conexao.sendall(data)
            
    except Exception as e:
        print(f"ERRO com {cliente}: {e}")
    finally:
        # Garante que a conexão com este cliente seja fechada
        conexao.close()
        print(f"CONEXÃO FECHADA com {cliente}")


def main():
    adicionarCtt("31971902735","Caio")


    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Exemplo Tkinter")

    # Cria um botão
    botao = tk.Button(janela, text="Clique Aqui", command=lambda: print("Botão clicado!"))
    botao.pack()  # Posiciona o botão na janela

    # Inicia o loop principal da interface gráfica
    janela.mainloop()
    
"""
    host = '127.0.0.1'  # Endereço IP do Servidor (localhost)
    porta = 5000        # Porta que o Servidor está ouvindo
    # Cria o soquete do servidor
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Vincula o soquete ao endereço e porta
        soquete.bind((host, porta))
        # Coloca o soquete em modo de escuta, aceitando até 5 conexões na fila
        soquete.listen(5)
        print(f"SERVIDOR OUVINDO em {host}:{porta}")
        while True:
            # Aceita uma nova conexão. Esta linha bloqueia até um cliente se conectar.
            conexao, cliente = soquete.accept()
            # Cria uma nova thread para cuidar do cliente recém-conectado
            # A função `handle_client` será executada nesta nova thread.
            client_thread = threading.Thread(target=handle_client, args=(conexao, cliente))
            client_thread.start()
            # Imprime o número de threads ativas (a principal + as dos clientes)
            print(f"CLIENTES ATIVOS: {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("\nSERVIDOR SENDO DESLIGADO...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fecha o soquete principal do servidor
        print("FECHANDO SOQUETE DO SERVIDOR.")
        soquete.close()
"""
        
        
# Bloco que garante que a função main() seja executada quando o script for rodado
if __name__ == "__main__":
    main()
