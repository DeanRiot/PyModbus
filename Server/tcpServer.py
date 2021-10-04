import socket
PORT = 3000
def decodeChar(dataString):
    byteArr = []
    for char in dataString:
        data = int(char,16)
        byteArr.append(data)
    return byteArr

h_name = socket.gethostname()
IP = socket.gethostbyname(h_name)
server = socket.socket()
server.bind(('localhost',PORT))
print("Сервер запущен! Адрес:", IP,"Порт: ",PORT)
server.listen(1)
connect,addr = server.accept()
print("соединение установелено")
while True:
    data = connect.recv(512)
    if not data:
        break
    print(data)
    print(data[1])
    inc=0
    for cr in data:
        print(hex(cr))
server.close()

