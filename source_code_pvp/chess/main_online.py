from game_data import *
from hosting import ServerHandler, ClientHandler

board = [
		 ["R", "K", "B", "Q", "E", "B", "K", "R"], 
		 ["P", "P", "P", "P", "P", "P", "P", "P"], 
		 [" ", " ", " ", " ", " ", " ", " ", " "], 
		 [" ", " ", " ", " ", " ", " ", " ", " "], 
		 [" ", " ", " ", " ", " ", " ", " ", " "], 
		 [" ", " ", " ", " ", " ", " ", " ", " "], 
		 ["P", "P", "P", "P", "P", "P", "P", "P"], 
		 ["R", "K", "B", "Q", "E", "B", "K", "R"]
		]

pieces = Initiator()
pos_handler = PositionHandler(pieces[0]+pieces[1])
p1 = Player("white", pieces[0])
p2 = Player("black", pieces[1])
player_handler = PlayerHandler(p1, p2)
end = False
checkmate = False
run = True
try:
	net = eval(input("Enter IP, Port: "))
	conn = input("Connect As server/client: ")
	if type(net[0]) == str and net[1] > 5000 and net[1] < 65000:
		if conn == "server":
			server = ServerHandler(*net)
			while run:
				if player_handler.current.team == "white":
					DisplayBoard(board)
					if checkmate:
						print("You're in Checkmate")
					print(player_handler.current.give_pieces_position())
					piece_pos = eval(input("Position of Piece: "))
					piece_to_go = eval(input("Position To Go: "))
					if PositionChecks(piece_pos) and PositionChecks(piece_to_go):
						piece = pos_handler.get_piece(piece_pos)
						if piece == False or piece.team != player_handler.current.team:
							print("Piece Position is Incorrect")
						else:
							check, piece, n_board = player_handler.play_piece(piece, piece_to_go, board, pos_handler)
							if check:
								board = n_board
								if piece != " ":
									pieces[2].append(piece)
									player_handler.remove_piece(piece)
								pos_handler = PositionHandler(player_handler.player1.pieces + player_handler.player2.pieces)
								end, lose_player = player_handler.game_end()
								checkmate = player_handler.checkmate(board, pos_handler)
								player_handler.change_player()
							else:
								print("Bad Position")
					else:
						print("Bad Position")
					# clear_screen()
					if end:
						break
						win_team = "white" if lose_player.team == "black" else "black"
				else:
					if checkmate:
						server.send_state(server.encode_state("", "", "You're in Checkmate"))
					server.send_state(server.encode_state(board, player_handler.current.give_pieces_position(), ""))
					server.send_state("input")
					pos_data = server.recv_inputs()
					pos_data = [list(p) for p in pos_data.split("\n")]
					print(pos_data)
					piece_pos = pos_data[0]
					piece_to_go = pos_data[1]
					if PositionChecks(piece_pos) and PositionChecks(piece_to_go):
						piece = pos_handler.get_piece(piece_pos)
						if piece == False or piece.team != player_handler.current.team:
							server.send_state(server.encode_state("", "", "Piece Position is Incorrect"))
						else:
							check, piece, n_board = player_handler.play_piece(piece, piece_to_go, board, pos_handler)
							if check:
								board = n_board
								if piece != " ":
									pieces[2].append(piece)
									player_handler.remove_piece(piece)
								pos_handler = PositionHandler(player_handler.player1.pieces + player_handler.player2.pieces)
								end, lose_player = player_handler.game_end()
								checkmate = player_handler.checkmate(board, pos_handler)
								player_handler.change_player()
							else:
								server.send_state(server.encode_state("", "", "Bad Position"))
					else:
						server.send_state(server.encode_state("", "", "Bad Position"))
					clear_screen()
					if end:
						win_team = "white" if lose_player.team == "black" else "black"
						break
			server.send_state(server.encode_state("", "", f"{win_team} Won The Match"))
			server.close_conn("end")
		else:
			client = ClientHandler(*net)
			while True:
				data = client.recv_data()
				if data == "end":
					break
				elif data == "ready":
					print("Game Started...")
				elif data == "input":
					print("hi")
					piece_pos = eval(input("Position of Piece: "))
					piece_to_go = eval(input("Position To Go: "))
					client.send_inputs(client.encode_inputs([piece_pos, piece_to_go]))
				else:
					data = data.split("\n")
					if board == "":
						print(data[-1])
					else:
						board = list(data[0])
						pieces = "\n".join(data[1:-1])
						DisplayBoard(board)
						print(pieces)
	else:
		print("[-] IP/Port is not Correctly Specified as rules.")
		print("[-] Ip should be like \"127.0.0.1\" and Port Should be Between 5000 and 65000")
		print("[-] Enter both like this \"127.0.0.1\", 9999")
		print("[-] Do It Correctly Next Time Bitch :]")
except KeyboardInterrupt:
	run = False