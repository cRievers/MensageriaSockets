import socket
import threading
import sqlite3
import tkinter as tk

def cadastro(numero, nome):
    if( ehValido(numero) and nome!= None):
        adicionarCtt(numero, nome)

def enviarMsgBroadCast(cursor, remetente, mensagem):
    cursor.execute("INSERT INTO mensagens (remetente_id, destinatario_id, conteudo) VALUES (?, NULL, '?');", (remetente, None, mensagem))

def adicionarCtt(cursor, numero, nome):
    cursor.execute("INSERT INTO clientes (numero, nome) VALUES (?, ?);", (numero, nome))

def criar_banco(cursor):
    cursor.execute('''
        CREATE TABLE clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            numero VARCHAR(20) UNIQUE NOT NULL,
            nome VARCHAR(100) NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE mensagens (
            id_mensagem INTEGER PRIMARY KEY AUTOINCREMENT,
            remetente_id INTEGER NOT NULL,
            destinatario_id INTEGER NULL, -- NULL para mensagens em grupo/broadcast
            conteudo TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            editada BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (remetente_id) REFERENCES clientes(id_cliente),
            FOREIGN KEY (destinatario_id) REFERENCES clientes(id_cliente)
        );
    ''')

def enviarMsg(cursor, remetente, destinatario, mensagem):
    cursor.execute("INSERT INTO mensagens (remetente_id, destinatario_id, conteudo) VALUES (?, ?, '?');", (remetente, destinatario, mensagem))

def apagarMsg(cursor, idMsg):
    cursor.execute("DELETE FROM mensagens WHERE id_mensagem = ?;", (idMsg))

def editarMsg(cursor, idMsg, novaMsg):
    cursor.execute("UPDATE mensagens SET conteudo = '[NOVO_CONTEUDO]', editada = TRUE WHERE id_mensagem = [ID_DA_MENSAGEM];", (novaMsg, idMsg))

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
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()

    #adicionarCtt(cursor, "31975839566","Alice")
    cursor.execute("SELECT * FROM clientes;")
    clientes = cursor.fetchall()
    print("Clientes cadastrados:")
    for cliente in clientes:
        print(cliente)

"""
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Exemplo Tkinter")

    # Cria um botão
    botao = tk.Button(janela, text="Clique Aqui", command=lambda: print("Botão clicado!"))
    botao.pack()  # Posiciona o botão na janela

    # Inicia o loop principal da interface gráfica
    janela.mainloop()
    

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
