import socket

def decodeChar(dataString):
    byteArr = []
    for char in dataString:
        data = int(char,16)
        byteArr.append(data)
    return byteArr

print("Сервер запущен")
server = socket.socket()
server.bind(('localhost',4000))
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
        if(inc==0):
        	inc+=1
        	continue
        print(cr)
server.close()

