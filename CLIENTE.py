import socket
host = '127.0.0.1'     # Endereco IP do Servidor
porta = 5000           # Porta que o Servidor esta
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (host, porta)
soquete.connect(destino)
msg = "Handshaking"
while(msg != ""):
    soquete.send(msg.encode("utf-8"))
    print("Insira uma msg: ")
    msg = input()
soquete.close()

