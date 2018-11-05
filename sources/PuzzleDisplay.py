# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PuzzleDisplay.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/18 13:56:25 by mressier          #+#    #+#              #
#    Updated: 2018/09/18 13:56:26 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Puzzle import *
from PuzzleIndex import *
import pygame

class Color:
	white = [255, 255, 255]
	black = [0, 0, 0]
	red = [255, 0, 0]

class Config:
	square_size = 100
	padding = 5
	font = None

class PuzzleDisplay:

	def __init__(self, puzzle):
		pygame.init()

		self.done = False
		self.puzzle = puzzle
		self.init_screen()

		while self.done is False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True

			pygame.display.flip()

		return

	def init_screen(self):
		self.screen_size = self.puzzle.size * Config.square_size + (self.puzzle.size + 1) * Config.padding
		self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
		self.screen.fill(Color.black)
		self.init_puzzle_on_screen()
		self.Config.font = pygame.font.SysFont("comicsansms", 16)

		pygame.display.update()
		
		return

	def init_puzzle_on_screen(self):
		index = PuzzleIndex(0, 0)

		for i in range(self.puzzle.size):
			index.column = 0
			index.line += Config.padding
			for j in range(self.puzzle.size):
				index.column += Config.padding
				pygame.draw.rect(self.screen, Color.white, pygame.Rect(index.column, index.line, Config.square_size, Config.square_size))
				index.column += Config.square_size
			index.line += Config.square_size
		return

## EXAMPLE
from PuzzleGenerator import *

for i in range(2, 10):
	display = PuzzleDisplay(puzzle_generator.generate_puzzle(i))
