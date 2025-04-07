# Echo client program
import socket

HOST = '192.168.56.1'     # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        resposta = input("Local: ").encode("utf-8")
        s.sendall(resposta)
        data = s.recv(1024)
        if not data: break
        print('Remot: ', data.decode("utf-8"))
