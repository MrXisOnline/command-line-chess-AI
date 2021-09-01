import socket
# from hosting import ClientHandler

# client = ClientHandler("127.0.0.1", 9999)
# print(client.recv_inputs())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9999))
data = client.recv(1024)
print(data.decode("utf-8"))
data = client.recv(1024)
print(data.decode("utf-8"))
client.close()