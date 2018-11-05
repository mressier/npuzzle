# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    puzzle.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/17 14:15:22 by mressier          #+#    #+#              #
#    Updated: 2018/09/17 14:15:24 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PuzzleMovement import PuzzleMovement
from PuzzleIndex import PuzzleIndex

class Puzzle:
	"""" Represent a NPuzzle grid """

	'Static variable'
	empty_piece = 0

	"""
	Init a puzzle.
	A puzzle must be a list of list as
	[[1, 0, 3],
	 [4, 5, 6],
	 [7, 8, 2]]
	of which size you want, as long as it's a square
	"""
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.size = len(puzzle)
		self.value_max = self.size**2
		self.hash = str(puzzle).__hash__()
	
	def __str__(self):
		string = ''
		for line in self.puzzle:
			if len(string) is not 0:
				string += '\n'
			for piece in line:
				if self.size < 10:
					string += str('%(number)3d' % {"number": piece})
				else:
					string += str('%(number)5d' % {"number": piece})
				string += ' '
		return string

	'Get the index of the piece with the given value if it exist'
	def get_piece_index(self, value):
		for line_index in range(self.size):
			try:
				col_index = self.puzzle[line_index].index(value)
				break
			except:
				col_index = None
		
		if line_index is None or col_index is None:
			return None
		return PuzzleIndex(line_index, col_index)

	def get_value_at_index(self, index):
		return self.puzzle[index.line][index.column]
	
	def set_value_at_index(self, index, value):
		self.puzzle[index.line][index.column] = value
		return

	'Get the movement available on the piece of value in the puzzle'
	def get_available_movements(self, piece_value):
		piece_index = self.get_piece_index(piece_value)

		if piece_index is None:
			return

		available_movements = []
		if piece_index.line > 0:
			available_movements.append(PuzzleMovement.up)
		if piece_index.column > 0:
			available_movements.append(PuzzleMovement.left)
		if piece_index.line + 1 < self.size:
			available_movements.append(PuzzleMovement.down)
		if piece_index.column + 1 < self.size:
			available_movements.append(PuzzleMovement.right)

		return available_movements

	'Apply movement on the empty piece of the puzzle'
	def apply_movement(self, piece_value, move):
		piece_index = self.get_piece_index(piece_value)

		if piece_index is None:
			return

		options = {
			PuzzleMovement.up: self.up,
			PuzzleMovement.down: self.down,
			PuzzleMovement.left: self.left,
			PuzzleMovement.right: self.right,
		}

		options[move](piece_index)
		self.hash = str(self.puzzle).__hash__()
		return

	'Move the piece at index up'
	def up(self, index):
		if index.line > 0:
			self.swap_piece(index, PuzzleIndex(index.line - 1, index.column))
		return
	
	'Move the piece at index down'
	def down(self, index):
		if index.line + 1 < self.size:
			self.swap_piece(index, PuzzleIndex(index.line + 1, index.column))
		return
	
	'Move the piece at index to the left'
	def left(self, index):
		if index.column > 0:
			self.swap_piece(index, PuzzleIndex(index.line, index.column - 1))
		return
	
	'Move the piece at index to the right'
	def right(self, index):
		if index.column + 1 < self.size:
			self.swap_piece(index, PuzzleIndex(index.line, index.column + 1))
		return

	def swap_piece(self, index1, index2):
		value1 = self.get_value_at_index(index1)
		value2 = self.get_value_at_index(index2)

		self.set_value_at_index(index1, value2)
		self.set_value_at_index(index2, value1)


## EXAMPLES
# puzzle = Puzzle([
# 	[1, 0, 3],
# 	[4, 5, 6],
# 	[7, 8, 2]
# ])

# print puzzle
# puzzle.apply_movement(Puzzle.empty_piece, PuzzleMovement.down)
# print puzzle
# print str(puzzle.get_available_movements(Puzzle.empty_piece))
