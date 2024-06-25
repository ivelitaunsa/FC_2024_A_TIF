import pygame as py
from constants import*

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
        self._displayText("[FPS] : " + str(FPS), self.win, (WIDTH - 120, 25), 14, GREEN)
        self._displayText("[CLICK DERECHO SUPERFICIE]", self.win, (WIDTH - 120, 40), 14, YELLOW)
        self._displayText("[CLICK IZQUIERDO AGUA]", self.win, (WIDTH - 120, 55), 14, YELLOW)
        self._displayText("[R PARA REINICIAR]", self.win, (WIDTH - 120, 70), 14, YELLOW)
        self._displayText("[ESC PARA SALIR]", self.win, (WIDTH - 120, 85), 14, YELLOW)

    
    def draw_main(self):
        self._displayText("PRESIONA ESPACIO PARA EMPEZAR", self.win, (WIDTH / 2, HEIGHT / 2), 30, YELLOW)
        py.display.update()

    def _displayText(self, theTextToDisplay, theDisplay, where, font_size, color):
        messageFont = py.font.Font('assets/VCR_OSD_MONO_1.001.ttf', font_size)
        messageSurf = messageFont.render(theTextToDisplay, True, color)
        messagePos = messageSurf.get_rect(center = where)
        theDisplay.blit(messageSurf, messagePos)
         

