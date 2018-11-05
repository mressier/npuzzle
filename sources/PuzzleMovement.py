# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PuzzleMovement.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/17 16:00:49 by mressier          #+#    #+#              #
#    Updated: 2018/09/17 16:01:05 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PuzzleMovement():
	up = "up"
	down = "down"
	left = "left"
	right = "right"

	def opposite(self, move):
		opposite = {
			PuzzleMovement.up: PuzzleMovement.down,
			PuzzleMovement.down: PuzzleMovement.up,
			PuzzleMovement.left: PuzzleMovement.right,
			PuzzleMovement.right: PuzzleMovement.left
		}
		return opposite[move]

puzzle_movement = PuzzleMovement()
