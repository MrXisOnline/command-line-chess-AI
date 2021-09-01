
class ChessPiece:
	def __init__(self, position):
		if position[0] == 0:
			self.team = "white"
		else:
			self.team = "black"

	def valid_moves(self, board, pos_handler):
		pass

	def play_move(self, position, board, pos_handler):
		all_moves = self.valid_moves(board, pos_handler)
		print("Possible moves was", [i[0] for i in all_moves])
		if position in [i[0] for i in all_moves]:
			board[self.position[0]][self.position[1]] = " "
			board[position[0]][position[1]] = self.symbol
			self.position = position
			return True, board
		else:
			return False, board

class Pawn(ChessPiece):
	def __init__(self, position):
		super().__init__(position)
		self.symbol = "P"
		self.name = "Pawn"
		if position[0] == 0:
			self.position = (6, position[1])
		else:
			self.position = (1, position[1])

	def valid_moves(self, board, pos_handler):
		if self.team == "white":
			all_moves = []
			check_pawn_front = True if self.position[0] != 0 else False
			check_pawn_left = True if self.position[1] != 0 else False
			check_pawn_right = True if self.position[1] != 7 else False
			if check_pawn_front:
				front_clear = True if board[self.position[0]-1][self.position[1]] == " " else False
				if front_clear:
					all_moves.append([(self.position[0]-1,self.position[1]), " "])
			if check_pawn_left:
				left_diagonal_clear = True if board[self.position[0]-1][self.position[1]-1] == " " else False
				if left_diagonal_clear:
					pass
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1, self.position[1]-1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1, self.position[1]-1), piece_at_pos])
			if check_pawn_right:
				right_diagonal_clear = True if board[self.position[0]-1][self.position[1]+1] == " " else False
				if right_diagonal_clear:
					pass
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1,self.position[1]+1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1,self.position[1]+1), piece_at_pos])
			return all_moves
		else:
			all_moves = []
			check_pawn_front = True if self.position[0] != 7 else False
			check_pawn_left = True if self.position[1] != 0 else False
			check_pawn_right = True if self.position[1] != 7 else False
			if check_pawn_front:
				front_clear = True if board[self.position[0]+1][self.position[1]] == " " else False
				if front_clear:
					all_moves.append([(self.position[0]+1,self.position[1]), " "])
			if check_pawn_left:
				left_diagonal_clear = True if board[self.position[0]+1][self.position[1]-1] == " " else False
				if left_diagonal_clear:
					pass
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1, self.position[1]-1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1,self.position[1]-1), piece_at_pos])
			if check_pawn_right:
				right_diagonal_clear = True if board[self.position[0]+1][self.position[1]+1] != " " else False
				if right_diagonal_clear:
					pass
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1,self.position[1]+1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1,self.position[1]+1), piece_at_pos])
			return all_moves

class Rook(ChessPiece):
	def __init__(self, position):
		super().__init__(position)
		self.symbol = "R"
		self.name = "Rook"
		if position[0] == 0:
			self.position = (7, position[1])
		else:
			self.position = (0, position[1])

	def valid_moves(self, board, pos_handler):
		all_moves = []
		check_rook_front = True if self.position[0] != 0 else False
		check_rook_left = True if self.position[1] != 0 else False
		check_rook_right = True if self.position[1] != 7 else False
		check_rook_bottom = True if self.position[0] != 7 else False
		if check_rook_front:
			r = self.position[0]
			for p in range(r):
				front_clear = True if board[self.position[0]-1-p][self.position[1]] == " " else False
				if front_clear:
					all_moves.append([(self.position[0]-1-p, self.position[1]), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1, self.position[1]-1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1,self.position[1]-1), piece_at_pos])
					break
		if check_rook_left:
			r = self.position[1]
			for p in range(r):
				left_side_clear = True if board[self.position[0]][self.position[1]-1-p] == " " else False
				if left_side_clear:
					all_moves.append([(self.position[0], self.position[1]-1-p), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0], self.position[1]-1-p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0], self.position[1]-1-p), piece_at_pos])
					break
		if check_rook_right:
			r = 7-self.position[1]
			for p in range(r):
				right_side_clear = True if board[self.position[0]][self.position[1]+1+p] == " " else False
				if right_side_clear:
					all_moves.append([(self.position[0], self.position[1]+1+p), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0], self.position[1]+1+p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0], self.position[1]+1+p), piece_at_pos])
					break
		if check_rook_bottom:
			r = 7-self.position[0]
			for p in range(r):
				bottom_clear = True if board[self.position[0]+1+p][self.position[1]] == " " else False
				if bottom_clear:
					all_moves.append([(self.position[0]+1+p, self.position[1]), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1+p, self.position[1]))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1+p, self.position[1]), piece_at_pos])
					break
		return all_moves

class Bishop(ChessPiece):
	def __init__(self, position):
		super().__init__(position)
		self.symbol = "B"
		self.name = "Bishop"
		if position[0] == 0:
			self.position = (7, position[1])
		else:
			self.position = (0, position[1])

	def valid_moves(self, board, pos_handler):
		all_moves = []
		check_bishop_up_left = True if self.position[0] != 0 else False
		check_bishop_up_right = True if self.position[0] != 0 else False
		check_bishop_down_left = True if self.position[0] != 7 else False
		check_bishop_down_right = True if self.position[0] != 7 else False
		if check_bishop_up_left:
			p = 0
			pos_check = self.position
			while pos_check[1] > 0 and pos_check[1] <= 7:
				post_check = self.position[0]-1-p >= 0 and self.position[0]-1-p <= 7 and self.position[1]-1-p >= 0 and self.position[1]-1-p <= 7
				if not post_check:
					break
				left_clear = True if board[self.position[0]-1-p][self.position[1]-1-p] == " " else False
				if left_clear:
					all_moves.append([(self.position[0]-1-p, self.position[1]-1-p), " "])
					pos_check = (self.position[0]-1-p, self.position[1]-1-p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1-p, self.position[1]-1-p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1-p, self.position[1]-1-p), piece_at_pos])
					break
		if check_bishop_up_right:
			p = 0
			pos_check = self.position
			while pos_check[1] >= 0 and pos_check[1] < 7:
				post_check = self.position[0]-1-p >= 0 and self.position[0]-1-p <= 7 and self.position[1]+1+p >= 0 and self.position[1]+1+p <= 7
				if not post_check:
					break
				right_clear = True if board[self.position[0]-1-p][self.position[1]+1+p] == " " else False
				if right_clear:
					all_moves.append([(self.position[0]-1-p, self.position[1]+1+p), " "])
					pos_check = (self.position[0]-1-p, self.position[1]+1+p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1-p, self.position[1]+1+p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1-p, self.position[1]+1+p), piece_at_pos])
					break
		if check_bishop_down_left:
			p = 0
			pos_check = self.position
			while pos_check[1] > 0 and pos_check[1] <= 7:
				post_check = self.position[0]+1+p >= 0 and self.position[0]+1+p <= 7 and self.position[1]-1-p >= 0 and self.position[1]-1-p <= 7
				if not post_check:
					break
				left_clear = True if board[self.position[0]+1+p][self.position[1]-1-p] == " " else False
				if left_clear:
					all_moves.append([(self.position[0]+1+p, self.position[1]-1-p), " "])
					pos_check = (self.position[0]+1+p, self.position[1]-1-p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1+p, self.position[1]-1-p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1+p, self.position[1]-1-p), piece_at_pos])
					break
		if check_bishop_down_right:
			p = 0
			pos_check = self.position
			while pos_check[1] >= 0 and pos_check[1] < 7:
				post_check = self.position[0]+1+p >= 0 and self.position[0]+1+p <= 7 and self.position[1]+1+p >= 0 and self.position[1]+1+p <= 7
				if not post_check:
					break
				right_clear = True if board[self.position[0]+1+p][self.position[1]+1+p] == " " else False
				if right_clear:
					all_moves.append([(self.position[0]+1+p, self.position[1]+1+p), " "])
					pos_check = (self.position[0]+1+p, self.position[1]+1+p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1+p, self.position[1]+1+p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1+p, self.position[1]+1+p), piece_at_pos])
					break
		return all_moves

class Knight(ChessPiece):
	def __init__(self, position):
		super().__init__(position)
		self.symbol = "K"
		self.name = "Knight"
		if position[0] == 0:
			self.position = (7, position[1])
		else:
			self.position = (0, position[1])

	def valid_moves(self, board, pos_handler):
		all_moves = []
		check_knight_up = True if self.position[0] != 0 else False
		check_knight_left = True if self.position[1] != 0 else False
		check_knight_right = True if self.position[1] != 7 else False
		check_knight_down = True if self.position[0] != 7 else False
		if check_knight_up:
			if self.position[0] == 1:
				pass
			else:
				up_left_clear = False
				up_right_clear = False
				if self.position[1] != 0:
					up_left_clear = True if board[self.position[0]-2][self.position[1]-1] == " " else False
					if up_left_clear:
						all_moves.append([(self.position[0]-2, self.position[1]-1), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]-2, self.position[1]-1))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]-2, self.position[1]-1), piece_at_pos])
				if self.position[1] != 7:
					up_right_clear = True if board[self.position[0]-2][self.position[1]+1] == " " else False
					if up_right_clear:
						all_moves.append([(self.position[0]-2, self.position[1]+1), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]-2, self.position[1]+1))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]-2, self.position[1]+1), piece_at_pos])
		if check_knight_left:
			if self.position[1] == 1:
				pass
			else:
				left_up_clear = False
				left_down_clear = False
				if self.position[0] != 0:
					left_up_clear = True if board[self.position[0]-1][self.position[1]-2] == " " else False
					if left_up_clear:
						all_moves.append([(self.position[0]-1, self.position[1]-2), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]-1, self.position[1]-2))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]+1, self.position[1]-2), piece_at_pos])
				if self.position[0] != 7:
					left_down_clear = True if board[self.position[0]+1][self.position[1]-2] == " " else False
					if left_down_clear:
						all_moves.append([(self.position[0]+1, self.position[1]-2), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]+1, self.position[1]-2))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]+1, self.position[1]-2), piece_at_pos])
		if check_knight_right:
			if self.position[1] == 6:
				pass
			else:
				right_up_clear = False
				right_down_clear = False
				if self.position[0] != 0:
					right_up_clear = True if board[self.position[0]-1][self.position[1]+2] == " " else False
					if right_up_clear:
						all_moves.append([(self.position[0]-1, self.position[1]+2), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]-1, self.position[1]+2))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]-1, self.position[1]+2), piece_at_pos])
				if self.position[0] != 7:
					right_down_clear = True if board[self.position[0]+1][self.position[1]+2] == " " else False
					if right_down_clear:
						all_moves.append([(self.position[0]+1, self.position[1]+2), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]+1, self.position[1]+2))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]+1, self.position[1]+2), piece_at_pos])
		if check_knight_down:
			if self.position[0] == 6:
				pass
			else:
				down_left_clear = False
				down_right_clear = False
				if self.position[1] != 0:
					down_left_clear = True if board[self.position[0]+2][self.position[1]-1] == " " else False
					if down_left_clear:
						all_moves.append([(self.position[0]+2, self.position[1]-1), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]+2, self.position[1]-1))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]+2, self.position[1]-1), piece_at_pos])
				if self.position[1] != 7:
					down_right_clear = True if board[self.position[0]+2][self.position[1]+1] == " " else False
					if down_right_clear:
						all_moves.append([(self.position[0]+2, self.position[1]+1), " "])
					else:
						piece_at_pos = pos_handler.get_piece((self.position[0]+2, self.position[1]+1))
						if piece_at_pos == False:
							pass
						elif piece_at_pos.team != self.team:
							all_moves.append([(self.position[0]+2, self.position[1]+1), piece_at_pos])
		return all_moves

class Queen(ChessPiece):
	def __init__(self, position):
		super().__init__(position)
		self.symbol = "Q"
		self.name = "Queen"
		if position[0] == 0:
			self.position = (7, position[1])
		else:
			self.position = (0, position[1])

	def valid_moves(self, board, pos_handler):
		# straight moves
		all_moves = []
		check_queen_front = True if self.position[0] != 0 else False
		check_queen_left = True if self.position[1] != 0 else False
		check_queen_right = True if self.position[1] != 7 else False
		check_queen_bottom = True if self.position[0] != 7 else False
		if check_queen_front:
			r = self.position[0]
			for p in range(r):
				front_clear = True if board[self.position[0]-1-p][self.position[1]] == " " else False
				if front_clear:
					all_moves.append([(self.position[0]-1-p, self.position[1]), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1-p, self.position[1]))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1-p, self.position[1]), piece_at_pos])
					break
		if check_queen_left:
			r = self.position[1]
			for p in range(r):
				left_side_clear = True if board[self.position[0]][self.position[1]-1-p] == " " else False
				if left_side_clear:
					all_moves.append([(self.position[0], self.position[1]-1-p), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0], self.position[1]-1-p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0], self.position[1]-1-p), piece_at_pos])
					break
		if check_queen_right:
			r = 7-self.position[1]
			for p in range(r):
				right_side_clear = True if board[self.position[0]][self.position[1]+1+p] == " " else False
				if right_side_clear:
					all_moves.append([(self.position[0], self.position[1]+1+p), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0], self.position[1]+1+p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0], self.position[1]+1+p), piece_at_pos])
					break
		if check_queen_bottom:
			r = 7-self.position[0]
			for p in range(r):
				bottom_clear = True if board[self.position[0]+1+p][self.position[1]] == " " else False
				if bottom_clear:
					all_moves.append([(self.position[0]+1+p, self.position[1]), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1+p, self.position[1]))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1+p, self.position[1]), piece_at_pos])
					break
		check_queen_up_left = True if self.position[0] != 0 else False
		check_queen_up_right = True if self.position[0] != 0 else False
		check_queen_down_left = True if self.position[0] != 7 else False
		check_queen_down_right = True if self.position[0] != 7 else False
		if check_queen_up_left:
			p = 0
			pos_check = self.position
			while pos_check[1] > 0 and pos_check[1] <= 7:
				post_check = self.position[0]-1-p >= 0 and self.position[0]-1-p <= 7 and self.position[1]-1-p >= 0 and self.position[1]-1-p <= 7
				if not post_check:
					break
				left_clear = True if board[self.position[0]-1-p][self.position[1]-1-p] == " " else False
				if left_clear:
					all_moves.append([(self.position[0]-1-p, self.position[1]-1-p), " "])
					pos_check = (self.position[0]-1-p, self.position[1]-1-p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1-p, self.position[1]-1-p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1-p, self.position[1]-1-p), piece_at_pos])
					break
		if check_queen_up_right:
			p = 0
			pos_check = self.position
			while pos_check[1] >= 0 and pos_check[1] < 7:
				post_check = self.position[0]-1-p >= 0 and self.position[0]-1-p <= 7 and self.position[1]+1+p >= 0 and self.position[1]+1+p <= 7
				if not post_check:
					break
				right_clear = True if board[self.position[0]-1-p][self.position[1]+1+p] == " " else False
				if right_clear:
					all_moves.append([(self.position[0]-1-p, self.position[1]+1+p), " "])
					pos_check = (self.position[0]-1-p, self.position[1]+1+p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1-p, self.position[1]+1+p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1-p, self.position[1]+1+p), piece_at_pos])
					break
		if check_queen_down_left:
			p = 0
			pos_check = self.position
			while pos_check[1] > 0 and pos_check[1] <= 7:
				post_check = self.position[0]+1+p >= 0 and self.position[0]+1+p <= 7 and self.position[1]-1-p >= 0 and self.position[1]-1-p <= 7
				if not post_check:
					break
				left_clear = True if board[self.position[0]+1+p][self.position[1]-1-p] == " " else False
				if left_clear:
					all_moves.append([(self.position[0]+1+p, self.position[1]-1-p), " "])
					pos_check = (self.position[0]+1+p, self.position[1]-1-p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1+p, self.position[1]-1-p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1+p, self.position[1]-1-p), piece_at_pos])
					break
		if check_queen_down_right:
			p = 0
			pos_check = self.position
			while pos_check[1] >= 0 and pos_check[1] < 7:
				post_check = self.position[0]+1+p >= 0 and self.position[0]+1+p <= 7 and self.position[1]+1+p >= 0 and self.position[1]+1+p <= 7
				if not post_check:
					break
				right_clear = True if board[self.position[0]+1+p][self.position[1]+1+p] == " " else False
				if right_clear:
					all_moves.append([(self.position[0]+1+p, self.position[1]+1+p), " "])
					pos_check = (self.position[0]+1+p, self.position[1]+1+p)
					p += 1
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1+p, self.position[1]+1+p))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1+p, self.position[1]+1+p), piece_at_pos])
					break
		return all_moves

class Emperor(ChessPiece):
	def __init__(self, position):
		super().__init__(position)
		self.symbol = "E"
		self.name = "Emperor"
		if position[0] == 0:
			self.position = (7, position[1])
		else:
			self.position = (0, position[1])

	def valid_moves(self, board, pos_handler):
		all_moves = []
		check_emperor_up = True if self.position[0] != 0 else False
		check_emperor_left = True if self.position[1] != 0 else False
		check_emperor_right = True if self.position[1] != 7 else False
		check_emperor_down = True if self.position[0] != 7 else False
		check_emperor_up_left = True if self.position[0] != 0 else False
		check_emperor_up_right = True if self.position[0] != 0 else False
		check_emperor_down_left = True if self.position[0] != 7 else False
		check_emperor_down_right = True if self.position[0] != 7 else False
		if check_emperor_up:
			up_clear = True if board[self.position[0]-1][self.position[1]] == " " else False
			if up_clear:
				all_moves.append([(self.position[0]-1 ,self.position[1]), " "])
			else:
				piece_at_pos = pos_handler.get_piece((self.position[0]-1 ,self.position[1]))
				if piece_at_pos == False:
					pass
				elif piece_at_pos.team != self.team:
					all_moves.append([(self.position[0]-1 ,self.position[1]), piece_at_pos])
		if check_emperor_left:
			left_clear = True if board[self.position[0]][self.position[1]-1] == " " else False
			if left_clear:
				all_moves.append([(self.position[0] ,self.position[1]-1), " "])
			else:
				piece_at_pos = pos_handler.get_piece((self.position[0] ,self.position[1]-1))
				if piece_at_pos == False:
					pass
				elif piece_at_pos.team != self.team:
					all_moves.append([(self.position[0] ,self.position[1]-1), piece_at_pos])
		if check_emperor_right:
			right_clear = True if board[self.position[0]][self.position[1]+1] == " " else False
			if right_clear:
				all_moves.append([(self.position[0] ,self.position[1]+1), " "])
			else:
				piece_at_pos = pos_handler.get_piece((self.position[0] ,self.position[1]+1))
				if piece_at_pos == False:
					pass
				elif piece_at_pos.team != self.team:
					all_moves.append([(self.position[0] ,self.position[1]+1), piece_at_pos])
		if check_emperor_down:
			down_clear = True if board[self.position[0]+1][self.position[1]] == " " else False
			if down_clear:
				all_moves.append([(self.position[0]+1 ,self.position[1]), " "])
			else:
				piece_at_pos = pos_handler.get_piece((self.position[0]+1 ,self.position[1]))
				if piece_at_pos == False:
					pass
				elif piece_at_pos.team != self.team:
					all_moves.append([(self.position[0]+1 ,self.position[1]), piece_at_pos])
		if check_emperor_up_left:
			post_check = self.position[0]-1 >= 0 and self.position[0]-1 <= 7 and self.position[1]-1 >= 0 and self.position[1]-1 <= 7
			if not post_check:
				pass
			else:
				up_left_clear = True if board[self.position[0]-1][self.position[1]-1] == " " else False
				if up_left_clear:
					all_moves.append([(self.position[0]-1 ,self.position[1]-1), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1 ,self.position[1]-1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1 ,self.position[1]-1), piece_at_pos])
		if check_emperor_up_right:
			post_check = self.position[0]-1 >= 0 and self.position[0]-1 <= 7 and self.position[1]+1 >= 0 and self.position[1]+1 <= 7
			if not post_check:
				pass
			else:
				up_right_clear = True if board[self.position[0]-1][self.position[1]+1] == " " else False
				if up_right_clear:
					all_moves.append([(self.position[0]-1 ,self.position[1]+1), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]-1 ,self.position[1]+1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]-1 ,self.position[1]+1), piece_at_pos])
		if check_emperor_down_left:
			post_check = self.position[0]+1 >= 0 and self.position[0]+1 <= 7 and self.position[1]-1 >= 0 and self.position[1]-1 <= 7
			if not post_check:
				pass
			else:
				down_left_clear = True if board[self.position[0]+1][self.position[1]-1] == " " else False
				if down_left_clear:
					all_moves.append([(self.position[0]+1 ,self.position[1]-1), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1 ,self.position[1]-1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1 ,self.position[1]-1), piece_at_pos])
		if check_emperor_down_right:
			post_check = self.position[0]+1 >= 0 and self.position[0]+1 <= 7 and self.position[1]+1 >= 0 and self.position[1]+1 <= 7
			if not post_check:
				pass
			else:
				down_right_clear = True if board[self.position[0]+1][self.position[1]+1] == " " else False
				if down_right_clear:
					all_moves.append([(self.position[0]+1 ,self.position[1]+1), " "])
				else:
					piece_at_pos = pos_handler.get_piece((self.position[0]+1 ,self.position[1]+1))
					if piece_at_pos == False:
						pass
					elif piece_at_pos.team != self.team:
						all_moves.append([(self.position[0]+1 ,self.position[1]+1), piece_at_pos])

	def checkmate(self, opp_pieces, board, pos_handler):
		all_moves = []
		all_moves_org = []
		for piece in opp_pieces:
			moves = piece.valid_moves(board, pos_handler)
			if moves != None:
				all_moves.append(moves)
		for moves in all_moves:
			if len(moves) != 0:
				for move in moves:
					all_moves_org.append(move[0])
		if self.position in all_moves_org:
			return True
		return False

