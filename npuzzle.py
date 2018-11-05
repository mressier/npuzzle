#!/usr/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/17 13:05:54 by mressier          #+#    #+#              #
#    Updated: 2018/09/17 13:05:55 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import sys
from sources.Parser import parse_map
from sources.PuzzleGenerator import puzzle_generator
from sources.Env import env
from sources.Node import Node
from sources.Puzzle import Puzzle
from sources.Solver import *
from sources.Heuristiques import *
from sources.PuzzleCompare import *
from sources.DisplaySoluce import displaySoluce
from sources.Log import log

def get_heuristique_from_args(args):
	if args.manhattan:
		return HeuristiquesType.manhattan
	elif args.melange:
		return HeuristiquesType.melange
	else:
		return HeuristiquesType.manhattan_square

def get_first_puzzle_from_args(args):
	if args.file:
		return parse_map(args.file)
	elif args.stdin:
		return parse_map(sys.stdin)
	else:
		return puzzle_generator.generate_random_puzzle(env.size)

""" Add arguments parsing """

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-f", "--file", type=file, help="read map from file")
group.add_argument("-i", "--stdin", action="store_true", help="read map on standard input")
group.add_argument('map_size', type=int, nargs='?', default=3,
					help='the size of the map we want to create (default 3)')

group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-e1","--manhattan", action="store_true", help="heuristique manhattan")
group2.add_argument("-e2","--melange", action="store_true", help="heuristique melange")
group2.add_argument("-e3","--manhattan_square", action="store_true", help="heuristique manhattan square (default)")

parser.add_argument("-s","--show_all", action="store_true", help="if show_all, solution step by step will be print on stdout")

try:
	args = parser.parse_args()
except IOError as e:
	log.error(e.filename + ": " + e.strerror)
	sys.exit(1)
except:
	sys.exit(1)


""" Create the first node from differents sources store it in the env class """

size = 0

log.verbose = False

if env.is_valid_size(args.map_size):
	env.size = args.map_size
else:
	log.error("Invalid map size: must be higher or equal than 2")
	sys.exit(1)

env.first_puzzle = get_first_puzzle_from_args(args)
env.add_open_node(Node(None, env.first_puzzle, None))

heuristiques.init(env.size)

log.default(env.first_puzzle)

last_node_solution = None
if puzzle_compare.is_solvable(env.first_puzzle, heuristiques.default_puzzle):
	heuristique = get_heuristique_from_args(args)
	last_node_solution = solver.get_puzzle_solution(heuristique)

if last_node_solution is None:
	log.error("unsolvable map ")
	sys.exit(1)

displaySoluce(args.show_all, last_node_solution)
sys.exit(0)
