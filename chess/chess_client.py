import socket
from hosting import ClientHandler
from game_data import DisplayBoard
import json

try:
	try:
		net = eval(input("Enter Server IP, Port: "))
	except KeyboardInterrupt:
		exit()
	if type(net[0]) == str and net[1] > 5000 and net[1] < 65000:
		client = ClientHandler(*net)
		while True:
			data = client.recv_data()
			if data == "end":
				break
			elif data == "input":
				try:
					piece_pos = eval(input("Position of Piece: "))
					piece_to_go = eval(input("Position To Go: "))
				except KeyboardInterrupt:
					break
				client.send_inputs(client.encode_inputs([piece_pos, piece_to_go]))
			else:
				try:
					data = json.loads(data)
					if data["board"] == "":
						print(data["message"])
					else:
						board = data["board"]
						pieces = data["pieces"]
						# print(board)
						DisplayBoard(board)
						print(pieces)
				except json.decoder.JSONDecodeError:
					pass
	else:
		print("[-] IP/Port is not Correctly Specified as rules.")
		print("[-] Ip should be like \"127.0.0.1\" and Port Should be Between 5000 and 65000")
		print("[-] Enter both like this \"127.0.0.1\", 9999")
		print("[-] Do It Correctly Next Time Bitch :]")
except ConnectionResetError:
	print("Server Stopped")
except SyntaxError:
	client.server.close()
	print("Syntax Error")
