import world
import pygame as py
from constants import*
import graphic

py.init()
WIN = py.display.set_mode((WIDTH, HEIGHT))
newGraphic = graphic.Graphic(WIN)
py.display.set_caption("FLUID AUTOMATA")



# Posicion del ratón
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // ASIZE
    col = x // ASIZE
    return row, col

def main():
    run = True
    clock = py.time.Clock()
    running_simulation = False
    WIN.fill(WHITE)
    generates = False
    reinit = False
    newWorld = world.World()

    while run:
        clock.tick(FPS)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:  # Boton para salir de la simulación
                    run = False
                if event.key == py.K_SPACE: # Boton para iniciar o pausar la simulacion
                    running_simulation = not(running_simulation)
                if event.key == py.K_r: # Boton para reiniciar el canvas
                    print("Tu presionaste R")
                    newWorld.reinit()                

         
            if event.type == py.MOUSEBUTTONDOWN:
                generates = True            
            elif  event.type == py.MOUSEBUTTONUP:
                generates = False
        
        if generates:
            particle_type = py.mouse.get_pressed()
            pos = py.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
            newWorld.make_alive(row, col, particle_type)

        if running_simulation:
            newWorld.live_one_step()
            newGraphic.draw_automatas(newWorld.grid)
        else:
            newGraphic.draw_main()
    py.quit()

main()
