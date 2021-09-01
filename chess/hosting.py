# import threading
import socket

class ServerHandler:
	def __init__(self, IP, Port):
		server, client = self.host(IP, Port)
		self.server = server
		self.client = client

	def host(self, IP, Port):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((IP, Port))
		server.listen(1)
		while True:
			print("[*] Waiting For Client")
			c, a = server.accept()
			print(f"[+] {a[0]}:{a[1]} Is Connected")
			break
		c.send(bytes("ready".encode("utf-8")))
		return server, c

	def encode_state(self, board="", pieces="", message=""):
		data = "\n".join([str(board), pieces, message])
		return data

	def send_state(self, data):
		self.client.send(bytes(data.encode("utf-8")))

	def recv_inputs(self):
		while True:
			data = self.client.recv(1024)
			if not data:
				break
		data = data.decode("utf-8")
		return data

	def close_conn(self, message):
		self.client.send(bytes(message.encode("utf-8")))
		self.client.close()


class ClientHandler:
	def __init__(self, Server, Port):
		self.server = self.connect(Server, Port)

	def connect(self, Server, Port):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.connect((Server, Port))
		data = server.recv(1024)
		data = data.decode("utf-8")
		if data == "ready":
			print(f"[+] Connected With {Server}:{Port}")
		return server

	def encode_inputs(self, data):
		return "\n".join([str(data[0]), str(data[1])])

	def recv_data(self):
		while True:
			data = self.server.recv(1024)
			if not data:
				break
		data = data.decode("utf-8")
		return data

	def send_inputs(self, data):
		self.server.send(bytes(data.encode("utf-8")))


# board = [
# 		 ["R", "K", "B", "Q", "E", "B", "K", "R"], 
# 		 ["P", "P", "P", "P", "P", "P", "P", "P"], 
# 		 [" ", " ", " ", " ", " ", " ", " ", " "], 
# 		 [" ", " ", " ", " ", " ", " ", " ", " "], 
# 		 [" ", " ", " ", " ", " ", " ", " ", " "], 
# 		 [" ", " ", " ", " ", " ", " ", " ", " "], 
# 		 ["P", "P", "P", "P", "P", "P", "P", "P"], 
# 		 ["R", "K", "B", "Q", "E", "B", "K", "R"]
# 		]
# server = ServerHandler("0.0.0.0", 9999)
# server.send_state(server.encode_state(board, "nothing pieces", ""))
# # client = ClientHandler("127)