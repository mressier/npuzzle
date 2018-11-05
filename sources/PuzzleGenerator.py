# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    RandomizePuzzle.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/18 10:53:01 by mressier          #+#    #+#              #
#    Updated: 2018/09/18 10:53:02 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Puzzle import *
from PuzzleIndex import *
from random import randint

class PuzzleGenerator:

	"""
	Generate a puzzle with a given size
	"""
	def generate_puzzle(self, size):
		if size < 2:
			return None
		
		puzzle = Puzzle(self.generate_empty_puzzle(size))
		index = PuzzleIndex(0, 0)
		value = 1

		while value < puzzle.value_max:
			# fill first line
			# ----
			# ....
			# ....
			# ....
			while index.column < size and puzzle.get_value_at_index(index) is 0 and value < puzzle.value_max:
				puzzle.set_value_at_index(index, value)
				value += 1
				index.column += 1
			
			# Go too far on right. Move left to the previous column.
			index.column -= 1
			# Move on the next line.
			index.line += 1

			# fill last column
			# xxxx
			# ...|
			# ...|
			# ...|
			while index.line < size and puzzle.get_value_at_index(index) is 0 and value < puzzle.value_max:
				puzzle.set_value_at_index(index, value)
				value += 1
				index.line += 1
			
			# Go too down. Move up to the previous line.
			index.line -= 1
			# Move left to the previous column.
			index.column -= 1

			# fill last line
			# xxxx
			# ...x
			# ...x
			# ----
			while index.column >= 0 and puzzle.get_value_at_index(index) is 0 and value < puzzle.value_max:
				puzzle.set_value_at_index(index, value)
				value += 1
				index.column -= 1
			
			# Go too far on left. Move right to the previous column.
			index.column += 1
			# Move up to the previous line
			index.line -= 1

			# fill first column
			# xxxx
			# |..x
			# |..x
			# xxxx
			while index.line >= 0 and puzzle.get_value_at_index(index) is 0 and value < puzzle.value_max:
				puzzle.set_value_at_index(index, value)
				value += 1
				index.line -= 1
			
			# Go too far up. Move down to the next line.
			index.line += 1
			# Move right to the next column.
			index.column += 1
		return puzzle

	"""
	Generate a random puzzle with a given size
	"""
	def generate_random_puzzle(self, size):
		puzzle = self.generate_puzzle(size)
		if puzzle is None:
			return

		nb_mixed = size ** 2 * 100

		for i in range(nb_mixed):
			scope = puzzle.get_available_movements(Puzzle.empty_piece)
			movement = scope[randint(0, len(scope) - 1)]
			puzzle.apply_movement(Puzzle.empty_piece, movement)
		return puzzle

	'Create a list of list of the given size fill of zero. It\'s an empty puzzle.'
	def generate_empty_puzzle(self, size):
		if size < 0:
			return None
		
		basic_puzzle = []
		for i in range(size):
			basic_puzzle.append([0] * size)
		return basic_puzzle

puzzle_generator = PuzzleGenerator()

## EXAMPLE
# ------ GENERATOR -------
# for i in range(1,5):
# 	print puzzle_generator.generate_puzzle(i)
# 	print "---"

# ------ RANDOMIZE ------
# for i in range(1,5):
# 	print puzzle_generator.generate_random_puzzle(i)
# 	print "---"
