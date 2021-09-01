from game_data import *

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
DisplayBoard(board)
run = True
try:
	while run:
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
		DisplayBoard(board)
		if end:
			break
			win_team = "white" if lose_player.team == "black" else "black"
	print(f"{win_team} Won The Match")
except KeyboardInterrupt:
	run = False