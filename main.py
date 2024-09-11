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
        self.font = pg.font.SysFont("Arial", 40)
        self.should_close = False
        self.state = 0 # 0 for game in progress 1 for game over
        self.snake = Snake()
        self.food = pg.Vector2(0, 0)
        self.new_food()

    def new_game(self):
        self.snake = Snake()
        self.new_food()
        self.state = 0

    def new_food(self):
        food = pg.Vector2(random.randint(0, N - 1) * SIZE, random.randint(0,  N - 1) * SIZE)
        while food in self.snake.get_body():
            food = pg.Vector2(random.randint(0, N - 1) * SIZE, random.randint(0,  N - 1) * SIZE)
        
        self.food = food

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        self.snake.update()

        if self.snake.check_food(self.food):
            self.new_food()

        if self.snake.check_death():
            self.state = 1
            self.snake.set_dir(0, 0)
        
    def draw(self):
        self.screen.fill(BACKGROUND)
        self.snake.draw(self.screen)
        pg.draw.rect(self.screen, RED, pg.Rect(self.food.x, self.food.y, SIZE, SIZE))

        if self.state == 1:
            pg.draw.rect(self.screen, RED, pg.Rect(0, 0, RES[0], RES[0]))

        score = self.snake.get_length()
        surf = self.font.render(str(score), True, WHITE)
        self.screen.blit(surf, (RES[0] - 40, 10))

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.should_close = True
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                x_dir, y_dir = self.snake.get_dir()
                if event.key == pg.K_w and y_dir == 0:
                    self.snake.set_dir(0, -1)
                
                elif event.key == pg.K_s and y_dir == 0:
                    self.snake.set_dir(0, 1)
                
                elif event.key == pg.K_a and x_dir == 0:
                    self.snake.set_dir(-1, 0)
                
                elif event.key == pg.K_d and x_dir == 0:
                    self.snake.set_dir(1, 0)

                if  self.state == 1 and event.key == pg.K_SPACE:
                    self.new_game()

    def run(self):
        while not self.should_close:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.new_game()
    game.run()