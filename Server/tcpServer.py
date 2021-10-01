import socket

def decodeChar(dataString):
    byteArr = []
    for char in dataString:
        data = int(char,16)
        byteArr.append(data)
    return byteArr

print("Сервер запущен")
server = socket.socket()
server.bind(('localhost',3000))
server.listen(1)
connect,addr = server.accept()
print("соединение установелено")
while True:
    data = connect.recv(512)
    if not data:
        break
    print(data)
    datastr = ' '
    for cr in decodeChar(data):
        datastr = datastr + ' ' + cr
    print(datastr)
server.close()

