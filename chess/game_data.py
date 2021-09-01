import os
from chess_pieces import Pawn, Rook, Bishop, Knight, Queen, Emperor

# diplay board
# board = [" ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 		 " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 		 " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 		 " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 		 " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 		 " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 		 " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 		 " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", "_", " ", 
# 		 "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", 
# 		 "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", 
# 


class PositionHandler:
	def __init__(self, all_pieces:list):
		self.all_pieces = all_pieces

	def get_piece(self, position):
		for piece in self.all_pieces:
			if piece.position == position:
				return piece
		return False

class Player:
	def __init__(self, team, pieces):
		self.team = team
		self.pieces = pieces

	def update_piece(self, pieces):
		self.pieces = pieces

	def give_pieces_position(self):
		return f"{self.team} team has :\n"+"\n".join([f"{pos.name} {pos.position}" for pos in self.pieces])


class PlayerHandler:
	def __init__(self, p1, p2):
		self.player1 = p1
		self.player1_king = p1.pieces[-1]
		self.player2 = p2
		self.player2_king = p2.pieces[-1]
		self.current = p1

	def change_player(self):
		if self.current == self.player1:
			self.current = self.player2
		else:
			self.current = self.player1

	def remove_piece(self, piece):
		team = piece.team
		if self.player1.team == team:
			all_pieces = self.player1.pieces
			all_pieces.pop(all_pieces.index(piece))
			self.player1.update_piece(all_pieces)
		else:
			all_pieces = self.player2.pieces
			all_pieces.pop(all_pieces.index(piece))
			self.player2.update_piece(all_pieces)

	def play_piece(self, piece, position, board, pos_handler):
		check, n_board = piece.play_move(position, board, pos_handler)
		if check:
			return True, piece, n_board
		else:
			return False, piece, n_board

	def checkmate(self, board, pos_handler):
		if self.current.team == self.player1.team:
			opp_pieces = self.player2.pieces
			player_king = self.current.pieces[-1]
			if player_king.symbol == "E":
				check = player_king.checkmate(opp_pieces, board, pos_handler)
				return check
			else:
				return False
		elif self.current.team == self.player2.team:
			opp_pieces = self.player1.pieces
			player_king = self.current.pieces[-1]
			if player_king.symbol == "E":
				check = player_king.checkmate(opp_pieces, board, pos_handler)
				return check
			else:
				return False

	def game_end(self):
		if self.player1_king not in self.player1.pieces:
			return True, self.player1
		elif self.player2_king not in self.player2.pieces:
			return True, self.player2
		else:
			return False, None



def DisplayBoard(board):
	row = 0
	print("  ", end="")
	for c in range(8):
		print(" "+str(c), end="")
	print()
	print("  ", end="")
	for _ in range(8):
		print(" _", end="")
	print()
	for i in range(1, 17):
		if i%2 == 1:
			cur_elements = board[row]
			print(str(row)+" ", end="")
			print("|", end="")
			cur_e_index = 0
			for i in range(8):
				print(cur_elements[cur_e_index]+"|", end="")
				cur_e_index += 1
			print()
			row += 1
		else:
			print("  |", end="")
			for _ in range(8):
				print("_|", end="")
			print()

def Initiator():
	white_pieces = []
	black_pieces = []
	for i in range(0, 8):
		white_pieces.append(Pawn((0, i)))
		black_pieces.append(Pawn((1, i)))
	white_pieces.append(Rook((0, 0)))
	black_pieces.append(Rook((1, 0)))
	white_pieces.append(Rook((0, 7)))
	black_pieces.append(Rook((1, 7)))
	white_pieces.append(Knight((0, 1)))
	black_pieces.append(Knight((1, 1)))
	white_pieces.append(Knight((0, 6)))
	black_pieces.append(Knight((1, 6)))
	white_pieces.append(Bishop((0, 2)))
	black_pieces.append(Bishop((1, 2)))
	white_pieces.append(Bishop((0, 5)))
	black_pieces.append(Bishop((1, 5)))
	white_pieces.append(Queen((0, 3)))
	black_pieces.append(Queen((1, 3)))
	white_pieces.append(Emperor((0, 4)))
	black_pieces.append(Emperor((1, 4)))
	return [white_pieces, black_pieces, []]

def PositionChecks(pos):
	if len(pos) == 2:
		if type(pos[0]) == int and type(pos[1]) == int:
			if (pos[0] >= 0 and pos[0] <= 7) and (pos[1] >= 0 and pos[1] <= 7):
				return True
	return False

def clear_screen():
	if os.name == "posix":
		os.system("clear")
	else:
		os.system("cls")
