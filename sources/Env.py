import sys
import math
from Log import log

class Env:

	def __init__(self):
		self.size = 0
		self.first_puzzle = None

		self.all_nodes = []
		self.opened_nodes = {0: []} # {heuristique_value: [nodes_with_this_heuristic]}

		self.closed_nodes_count = 0
		self.opened_nodes_count = 0
		self.nodes_count = 0

		self.max_opened_nodes = 0

	def is_valid_size(self, size):
		return size >= 2 and size < sys.maxint

	def close_node(self, node):
		self.opened_nodes[node.fn].remove(node)
		self.closed_nodes_count += 1
		self.opened_nodes_count -= 1

	def add_open_node(self, node):
		self.opened_nodes.setdefault(node.fn, [])
		self.smart_insert_node(node.fn, node)
		self.all_nodes.append(node)
		self.nodes_count += 1
		self.opened_nodes_count += 1

		if self.opened_nodes_count > self.max_opened_nodes:
			self.max_opened_nodes = self.opened_nodes_count

		return

	def smart_insert_node(self, node_list_index, node):
		"""
		Insert a node
		Nodes are sorted by hash value, from the lower to the higher
		"""

		max = len(self.opened_nodes[node_list_index])
		i = int(math.ceil(max / 2))

		limits = {"high": max - 1, "low": 0}

		while i <= limits["high"] and i >= limits["low"]:
			current_node = self.opened_nodes[node_list_index][i]
			if node == current_node:
				return
			
			if node > current_node:
				if i == max - 1:
					self.append_node(node_list_index, node)
					return

				# node is higher, search after
				limits["low"] = i
				dist_to_high = limits["high"] - i
				i += int(math.ceil(dist_to_high / 2.0))
			
			if node < current_node:
				prev_node = self.opened_nodes[node_list_index][i - 1] if i > 0 else None
				if prev_node is None or node > prev_node:
					self.insert_node(node_list_index, i, node)
					return

				# node is lower, search before
				limits["high"] = i
				dist_to_low = i - limits["low"]
				i -= int(math.ceil(dist_to_low / 2.0))

		# default
		self.append_node(node_list_index, node)
		return

	def append_node(self, node_list_index, node):
		self.opened_nodes[node_list_index].append(node)
		return

	def insert_node(self, node_list_index, index, node):
		self.opened_nodes[node_list_index].insert(index, node)
		return

	def get_smaller_nodes(self):
		smaller = None
		for (value, nodes) in self.opened_nodes.items():
			if smaller is None and len(nodes) > 0:
				smaller = value
			elif value < smaller and len(nodes) > 0:
				smaller = value
		return self.opened_nodes[smaller]

env = Env()