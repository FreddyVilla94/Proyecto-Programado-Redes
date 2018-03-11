import socket


def getHostName():
    hostName = socket.gethostname()                 #Nombre del Host
    return hostName

def getHostIP():
    hostName = getHostName()
    ipAddress = socket.gethostbyname(hostName)      # IP Address del Host
    return ipAddress

