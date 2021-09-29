# import threading
import socket
import json

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
		data = {"board": board,
				"pieces": pieces, 
				"message": message}
		return json.dumps(data)

	def send_state(self, data):
		self.client.send(bytes(data, "utf-8"))

	def recv_inputs(self):
		data = self.client.recv(1024)
		data = data.decode("utf-8")
		if not data:
			self.client.close()
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
			print("Game Started")
		return server

	def encode_inputs(self, data):
		inputs = {"piece_pos": data[0], 
				"piece_to_go": data[1]}
		return json.dumps(inputs)

	def recv_data(self):
		data = self.server.recv(1024)
		data = data.decode("utf-8")
		return data

	def send_inputs(self, data):
		self.server.send(bytes(data, "utf-8"))


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