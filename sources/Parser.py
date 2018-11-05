import re
import sys
from Log import log
from Node import Node
from Env import env
from Puzzle import Puzzle

def parse_map(map):
	first = True
		
	puzzle = []

	for line in map:
		line_util = line.split('#')[0]
		if line_util == None or line_util == "":
			continue
		if first is not True:
			puzzle.append(parse_line(line_util))
			if (len(puzzle) > env.size):
				log.error("parsing map. Too many lines")
				sys.exit(1)
		else:
			first = False
			parse_line(line_util)

	if (len(puzzle) < env.size):
		log.error("parsing map. Not Enought Lines")
		sys.exit(1)

	parse_map_value(puzzle)
	return Puzzle(puzzle)

def to_int(char):
	return int(char)

def parse_line(line):
	if (len(re.findall(r"([^\d\s]+)", line)) > 0):
		log.error("parsing line (bad character found) " + line)
		sys.exit(1)

	m = re.findall(r"(\s*-?\d+)", line)
	if (parse_line.first is True):
		parse_line.first = False
		if len(m) != 1:
			log.error("parsing map. First Line must be the map size")
			sys.exit(1)
		env.size = int(m[0])
		if not env.is_valid_size(env.size):
			log.error("Invalid map size: must be higher or equal than 2")
			sys.exit(1)
	else:
		if len(m) < env.size:
			log.error("parsing map. not enought numbers at line : " + line)
			sys.exit(1)
		elif len(m) > env.size:
			log.error("parsing map. too many numbers at line : " + line)
			sys.exit(1)
		return [ to_int(num) for num in m ]

parse_line.first = True


def parse_map_value(puzzle):
	value = [0] * (env.size * env.size)
	for line in puzzle:
		for num in line:
			if num >= env.size * env.size:
				log.error("parsing map. value find to high : " + str(num))
				sys.exit(1)
			if value[num] == 1:
				log.error("parsing map. value find multiple time : " + str(num))
				sys.exit(1)
			value[num] = 1
	return

