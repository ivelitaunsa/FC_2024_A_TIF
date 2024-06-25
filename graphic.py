import pygame as py
from constants import*
import random

class Graphic:
    def __init__(self, win):
        self.win = win
    
    def draw_automatas(self, grid):
        for x in range(xCells):
            for y in range(yCells):
                py.draw.rect(self.win, grid[x][y].color, (y * ASIZE, x * ASIZE, ASIZE, ASIZE))
        self._print_the_text()
        py.display.update()
    
    def _print_the_text(self):
        self._displayText("[FPS] : " + str(FPS), self.win, (WIDTH - 90, 25), 12, GREEN)
        self._displayText("[CLICK DERECHO SUPERFICIE]", self.win, (WIDTH - 90, 40), 12, YELLOW)
        self._displayText("[CLICK IZQUIERDO AGUA]", self.win, (WIDTH - 90, 55), 12, YELLOW)
        self._displayText("[R PARA REINICIAR]", self.win, (WIDTH - 90, 70), 12, YELLOW)
        self._displayText("[ESC PARA SALIR]", self.win, (WIDTH - 90, 85), 12, YELLOW)

    
    def draw_main(self):
        self._displayText("PRESIONA ESPACIO PARA EMPEZAR", self.win, (WIDTH / 2, HEIGHT / 2), 30, YELLOW)
        py.display.update()

    def _displayText(self, theTextToDisplay, theDisplay, where, font_size, color):
        messageFont = py.font.Font('assets/VCR_OSD_MONO_1.001.ttf', font_size)
        messageSurf = messageFont.render(theTextToDisplay, True, color)
        messagePos = messageSurf.get_rect(center = where)
        theDisplay.blit(messageSurf, messagePos)
         

