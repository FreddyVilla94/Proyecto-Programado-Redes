#cliente
import socket
import index

port = 6666

sock = socket.socket()

sock.connect((index.getHostIP(), port))

datos = sock.recv(4096)
print (datos.decode('utf-8'))



while True:


  message = input("envia un mensaje")
  sock.send(message.encode('utf-8'))




  if message == "quit":
    break
    print("bye")
    sock.close()