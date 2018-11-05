# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PuzzleCompare.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/18 14:32:39 by mressier          #+#    #+#              #
#    Updated: 2018/09/18 14:32:47 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Puzzle import *
import copy

class PuzzleCompare:
	"""
	Return the number of move needed to move the value's piece
	until its position on the puzzle_ref

	For example:

		puzzle ref:
			xxx
			x0x
			xxx
		puzzle_mixed:
			0xx
			xxx
			xxx

	for value '0' : return 2 because we need 2 move
	to put the 0 piece from the left corner to the center of the puzzle
	"""
	def nb_move_needed_for_value(self, value, puzzle_ref, puzzle_mixed):
		if puzzle_ref.size is not puzzle_mixed.size:
			return None
		
		index_ref = puzzle_ref.get_piece_index(value)
		index_mixed = puzzle_mixed.get_piece_index(value)

		if index_ref is None or index_mixed is None:
			return None
		
		return abs(index_ref.line - index_mixed.line) + abs(index_ref.column - index_mixed.column)

	"""
	Return the number of permutation needed to make
	the puzzle_mixed in the same configuration as the puzzle_ref.

	Indeed, the initial configuration of a npuzzle is a permutation of its final configuration.
	"""
	def nb_permutation_needed(self, puzzle_ref, puzzle_mixed):
		if puzzle_ref.size is not puzzle_mixed.size:
			return None
		
		copy_mixed = copy.deepcopy(puzzle_mixed)
		nb_permutation = 0

		for value in range(puzzle_ref.value_max):
			if self.is_value_on_ref_position(value, puzzle_ref, copy_mixed) is False:
				nb_permutation += 1
				self.put_value_on_ref_position(value, puzzle_ref, copy_mixed)
		return nb_permutation

	"""
	Take a look on wikipedia to understand

	If the parity of the number of move needed to put the empty piece on its reference position
	is the same as the parity of the number of permutation needed to put the puzzle on its reference configuration
	so the puzzle is solvable
	"""
	def is_solvable(self, initial_puzzle, final_puzzle):
		nb_move = self.nb_move_needed_for_value(Puzzle.empty_piece, initial_puzzle, final_puzzle)
		nb_permutation = self.nb_permutation_needed(initial_puzzle, final_puzzle)

		return nb_move % 2 is nb_permutation % 2

	'return true if the value is on the same position on both puzzles'
	def is_value_on_ref_position(self, value, puzzle_ref, puzzle_mixed):
		index_ref = puzzle_ref.get_piece_index(value)
		index_mixed = puzzle_mixed.get_piece_index(value)

		if index_ref is None or index_mixed is None:
			return False

		return index_ref.line is index_mixed.line and index_ref.column is index_mixed.column

	'put value on the position it should have on puzzle_mixed, compared with puzzle_ref'
	def put_value_on_ref_position(self, value, puzzle_ref, puzzle_mixed):
		index_ref = puzzle_ref.get_piece_index(value)
		index_mixed = puzzle_mixed.get_piece_index(value)

		if index_ref is None or index_mixed is None:
			return False
		
		puzzle_mixed.swap_piece(index_ref, index_mixed)
		return

puzzle_compare = PuzzleCompare()

## EXAMPLE
# from PuzzleGenerator import *

# size = 10
# puzzle = puzzle_generator.generate_puzzle(size)
# random_puzzle = puzzle_generator.generate_random_puzzle(size)

# print '----PUZZLE----'
# print puzzle
# print '----PUZZLE RAND----'
# print random_puzzle

# print 'NB MOVE : ' + str(puzzle_compare.nb_move_needed_for_value(0, puzzle, random_puzzle))
# print 'NB PERMUTATIONS : ' + str(puzzle_compare.nb_permutation_needed(puzzle, random_puzzle))
# print 'IS SOLVABLE : ' + str(puzzle_compare.is_solvable(puzzle, random_puzzle))

# print "\n----SWAP PIECE----\n"
# random_puzzle.swap_piece(PuzzleIndex(0, 0), PuzzleIndex(0, 1))
# print random_puzzle
# print '----'
# print 'NB MOVE : ' + str(puzzle_compare.nb_move_needed_for_value(0, puzzle, random_puzzle))
# print 'NB PERMUTATIONS : ' + str(puzzle_compare.nb_permutation_needed(puzzle, random_puzzle))
# print 'IS SOLVABLE : ' + str(puzzle_compare.is_solvable(puzzle, random_puzzle))
