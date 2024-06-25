# this class is a kind of automata
from automatas import*
import copy
from constants import*
import math

class Water(Automata):
    def __init__(self, xAddress, yAddress, mass = 0):
        super().__init__(xAddress, yAddress)        
        self.mass = mass
        self.id = 2
        self.color = BLUE

    def save_color(self):
        self.color = (0, 0, int(255 - self.mass*60))

class Ground(Automata): # Ground es solo para definir algo diferente al agua, en este caso forma parte de la estructura
    def __init__(self, xAddress, yAddress):
        super().__init__(xAddress, yAddress)
        self.color = BROWN_GROUND
        self.id = 3