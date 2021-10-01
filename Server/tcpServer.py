import socket
while True:
    try:    
        server = socket.socket()
        server.bind(('localhost',2470))
        server.listen(1)
        connect,addr = server.accept()
        print("соединение установелено")
        while True:
            data = connect.recv(512)
            if not data:
                break
            print(data)
    except:
        print('соединене потеряно')
        server.close()
