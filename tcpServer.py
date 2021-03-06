#servidor
import socket
import threading
import index

port = 9696

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")
sock.bind(("", port))
print ("socket bind complete")
sock.listen(20)
print ("socket now listening")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('conexion con %s:%s.'%(addr[0],addr[1]))
        conn.send("server: Hello client %s:%s".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print('Mensaje de {}\nAsunto: {}\n'.format(addr, datos.decode('utf-8')))

            else:
                print("prueba")
                break
    finally:
        conn.close()

while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()