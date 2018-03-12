#cliente
import socket
import index

host = "172.24.161.1"

port = 9696

sock = socket.socket()

sock.connect((host, port))

datos = sock.recv(4096)
print (datos.decode('utf-8'))



while True:


  message = input("envia un mensaje: ")
  sock.send(message.encode('utf-8'))




  if message == "quit":
    sock.send("Bye".encode('utf-8'))
    break

print("bye")
sock.close()