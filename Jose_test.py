import random

class Board:

    
          


    
          def __init__(self):
                    self.piles = []
                    self._prepare()
          
          def apply(self, move):
                    
                    
                    #must change to check if anything matches 
                    pile = move.get_pile()
                    stones = move.get_stones()
                    self._piles[pile] = max(0, self._piles[pile] - stones)
          
          
          
          def is_empty(self):
                    
                    
                    #must change to check if the sequence is the same
                    empty = [0] * len(self._piles)
                    return self._piles == empty

          def to_string(self):
                    
                    #display the colors, board
                    
                    text =  "\n--------------------"
                    for pile, stones in enumerate(self._piles):
                              text += (f"\n{pile}: " + "O " * stones)
                    text += "\n--------------------"
                    return text

          
                    #set up the board with a random order of colors
          def _prepare(self):
                    piles = ["r","g","y","b"]
                    Random_sequence =random.sample(piles, len(piles))
                    return Random_sequence
    

Board()
