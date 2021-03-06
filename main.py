import modb as modbus
import TCPClient as TCP

print('Введите ip-адрес')
addr =  input()
print('Введите порт')
port = int(input())

print("Попытка подключения к " + addr + ':' + str(port))

try:
    conn = TCP.Connect(addr, port)
    print("подключено успешно")
    print("Введите пакет modbus-rtu без crc")
except:
    print("Не удалось подключиться к "+addr + ':'+str(port))
    
while True:
    frame = input()
    if frame == "stop":
        break
    frame = modbus.createFrame(modbus.parseHexFrame(frame))
    dataBytes = bytes(frame)
    TCP.Send(dataBytes,conn)
    #data = TCP.Receive(conn,512)
TCP.Close(conn)
