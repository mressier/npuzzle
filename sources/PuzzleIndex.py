# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PuzzleIndex.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/18 10:44:36 by mressier          #+#    #+#              #
#    Updated: 2018/09/18 10:44:37 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PuzzleIndex:
	def __init__(self, line, column):
		self.line = line
		self.column = column

	def __str__(self):
		return 'line: ' + str(self.line) + ', col: ' + str(self.column)
