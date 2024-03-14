import pygame as pg
import sys
from settings import *
from map import *
from player import *


class Game: 
    def __init__(self): #initializes game
        pg.init
        self.screen =pg.display.set_mode(RES) #Renders screen resolution
        self.clock =pg.time.Clock()  #tick rate to control FPS
        self.delta_time = 1
        self.new_Game()

    def new_Game(self):
        self.map = Map(self)
    
    def update(self):
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type ==pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
    

    