from game_data import *
from hosting import ServerHandler, ClientHandler
import json

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
win_team = None
checkmate = False
try:
	try:
		net = eval(input("Enter Server IP, Port to Host: "))
	except KeyboardInterrupt:
		exit()
	if type(net[0]) == str and net[1] > 5000 and net[1] < 65000:
		server = ServerHandler(*net)
		DisplayBoard(board)
		while True:
			error_msg = ""
			if player_handler.current.team == "white":
				if checkmate:
					error_msg = "You're in Checkmate"
				print(player_handler.current.give_pieces_position())
				try:
					piece_pos = eval(input("Position of Piece: "))
					piece_to_go = eval(input("Position To Go: "))
				except KeyboardInterrupt:
					break
				if PositionChecks(piece_pos) and PositionChecks(piece_to_go):
					piece = pos_handler.get_piece(piece_pos)
					if piece == False or piece.team != player_handler.current.team:
						error_msg = "Piece Position is Incorrect"
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
							error_msg = "Bad Position"
				else:
					error_msg = "Bad Position"
				clear_screen()
				DisplayBoard(board)
				print(error_msg)
				if end:
					break
					win_team = "white" if lose_player.team == "black" else "black"
			else:
				if checkmate:
					server.send_state(server.encode_state("", "", "You're in Checkmate"))
				server.send_state(server.encode_state(board, player_handler.current.give_pieces_position(), ""))
				server.send_state("input")
				pos_data = server.recv_inputs()
				try:
					pos_data = json.loads(pos_data)
					print(pos_data)
					piece_pos = tuple(pos_data["piece_pos"])
					piece_to_go = tuple(pos_data["piece_to_go"])
					if PositionChecks(piece_pos) and PositionChecks(piece_to_go):
						piece = pos_handler.get_piece(piece_pos)
						print(piece)
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
								server.send_state(server.encode_state(board, "", ""))
							else:
								server.send_state(server.encode_state("", "", "Bad Position"))
					else:
						server.send_state(server.encode_state("", "", "Bad Position"))
					# clear_screen()
					if end:
						win_team = "white" if lose_player.team == "black" else "black"
						break
					clear_screen()
					DisplayBoard(board)
				except json.decoder.JSONDecodeError:
					pass
		server.send_state(server.encode_state("", "", f"{win_team} Won The Match"))
		server.close_conn("end")
	else:
		print("[-] IP/Port is not Correctly Specified as rules.")
		print("[-] Ip should be like \"127.0.0.1\" and Port Should be Between 5000 and 65000")
		print("[-] Enter both like this \"127.0.0.1\", 9999")
		print("[-] Do It Correctly Next Time Bitch :]")
except ConnectionResetError:
	print("Client Disconnected")
except SyntaxError:
	server.close_conn("end")
	print("Syntax Error")