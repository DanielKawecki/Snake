import pygame as pg
import sys
import random
from settings import *
from snake import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.should_close = False
        self.snake = Snake()
        self.food = pg.Vector2(0, 0)
        self.new_food()

    def new_game(self):
        pass

    def new_food(self):
        self.food = pg.Vector2(random.randint(0, 29) * SIZE, random.randint(0, 29) * SIZE)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        self.snake.update()

        if self.snake.check_food(self.food):
            self.new_food()
        
    def draw(self):
        self.screen.fill(BACKGROUND)
        self.snake.draw(self.screen)
        pg.draw.rect(self.screen, RED, pg.Rect(self.food.x, self.food.y, SIZE, SIZE))

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.should_close = True
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.snake.set_dir(0, -1)
                
                elif event.key == pg.K_s:
                    self.snake.set_dir(0, 1)
                
                elif event.key == pg.K_a:
                    self.snake.set_dir(-1, 0)
                
                elif event.key == pg.K_d:
                    self.snake.set_dir(1, 0)

    def run(self):
        while not self.should_close:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.new_game()
    game.run()