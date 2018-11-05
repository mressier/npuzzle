
from Puzzle import Puzzle
from Node import Node
from Env import env
from Log import log
from Heuristiques import *
from PuzzleMovement import *
import sys
import copy

class Solver:

	def __init__(self):
		self.fn_last_min = sys.maxint

	def find_tree_solution(self):
		count = 0
		while (42):
			count += 1
			if count % 1000 is 0:
				log.debug(str(count)
				+ ' tries -> nodes : ' + str(env.nodes_count)
				+ ', opened : ' + str(env.nodes_count- env.closed_nodes_count))

			node = self.find_viable_node_with_a_star()
			if node is None:
				return None

			if self.is_solution(node):
				return node

			available_movements = node.puzzle.get_available_movements(Puzzle.empty_piece)

			for move in available_movements:
				if node.movement and move is puzzle_movement.opposite(node.movement):
					continue
				new_puzzle = copy.deepcopy(node.puzzle)
				new_puzzle.apply_movement(Puzzle.empty_piece, move)
				
				new_node = Node(node, new_puzzle, move)
				env.add_open_node(new_node)
			env.close_node(node)

		return None

	def find_viable_node_with_a_star(self):
		smaller_nodes = env.get_smaller_nodes()
		if smaller_nodes:
			return smaller_nodes[0]
		return None

	def is_solution(self, node):
		return node.dist_heuristic is 0

	def get_puzzle_solution(self, heuristic):
		heuristiques.change_heuristique(heuristic)

		# if self.is_solution(env.first_puzzle):
		# 	return env.first_puzzle

		return self.find_tree_solution()

solver = Solver()
