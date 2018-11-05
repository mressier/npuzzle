
from Puzzle import Puzzle
from PuzzleGenerator import puzzle_generator
from PuzzleCompare import puzzle_compare

class Heuristiques:

    def __init__(self):
        self.current_heuristique = HeuristiquesType.manhattan
        self.default_puzzle = None
        self.default_is_before_table = []

    """ PRIVATE METHODS """

    def create_before_table(self, puzzle):
        ret = []
        for i in range(puzzle.size**2):
            for j in range(i, puzzle.size**2):
                if i != j:
                    ret.append(
                        self.is_before(
                            puzzle.get_piece_index(i),
                            puzzle.get_piece_index(j)
                        )
                    )
        return ret

    def is_before(self,index1, index2):
        if index1.line == index2.line:
            return index1.column < index2.column
        return index1.line < index2.line


    def check_default(self , puzzle):
        if self.default_puzzle == None or self.default_puzzle.size != puzzle.size:
            self.default_puzzle = puzzle_generator.generate_puzzle(puzzle.size)
        if self.current_heuristique == HeuristiquesType.melange and len(self.default_is_before_table) == 0:
            self.default_is_before_table = self.create_before_table(self.default_puzzle)

    def manhattan(self, puzzle):
        self.check_default(puzzle)
        tot = 0
        for i in range(1, puzzle.size * puzzle.size):
            dist = puzzle_compare.nb_move_needed_for_value(i, self.default_puzzle, puzzle)
            tot += dist
        return tot

    def manhattan_square(self, puzzle):
        self.check_default(puzzle)
        tot = 0
        for i in range(1, puzzle.size * puzzle.size):
            dist = puzzle_compare.nb_move_needed_for_value(i, self.default_puzzle, puzzle)
            tot += dist**2
        return tot

    def melange(self, puzzle):
        self.check_default(puzzle)
        puzzle_before_table = self.create_before_table(puzzle)
        tot = 0
        for i in range(len(puzzle_before_table)):
            if puzzle_before_table[i] != self.default_is_before_table[i]:
                tot += 1
        return tot

    """ PUBLIC METHODS """

    def init(self, puzzle_size):
        self.default_puzzle = puzzle_generator.generate_puzzle(puzzle_size)
        

    def change_heuristique(self, heuristique):
        if self.current_heuristique is not heuristique:
            self.current_heuristique = heuristique
            self.default_is_before_table = []

    def calcul_heuristique(self, puzzle):
        tab = {
            HeuristiquesType.manhattan : self.manhattan,
            HeuristiquesType.melange : self.melange,
            HeuristiquesType.manhattan_square: self.manhattan_square
        }
        return tab[self.current_heuristique](puzzle)


    
class HeuristiquesType:
    manhattan = "manhattan"
    melange = "melange"
    manhattan_square = "manhattan_square"

heuristiques = Heuristiques()
