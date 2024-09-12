import pygame as pg
import sys
import random
from settings import *
from snake import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((RES, RES))
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("FFF Forward", 18)
        self.should_close = False
        self.state = 0 # 0 for game in progress 1 for game over
        self.snake = Snake()
        self.food = pg.Vector2(0, 0)
        self.new_food()
        self.score = 0

        self.last_time = 0
        self.update_interval = 1000 // FPS

        pg.display.set_caption("SNAKE")
        pg.display.set_icon(pg.image.load("resources/snake.png"))

    def new_game(self):
        self.snake = Snake()
        self.new_food()
        self.state = 0
        self.score = 0

    def new_food(self):
        food = pg.Vector2(random.randint(2, N + 1) * SIZE, random.randint(2,  N + 1) * SIZE)
        while food in self.snake.get_body():
            food = pg.Vector2(random.randint(2, N + 1) * SIZE, random.randint(2,  N + 1) * SIZE)
        
        self.food = food

    def update(self):
        pg.display.flip()
        current_time = pg.time.get_ticks()
        if current_time - self.last_time >= self.update_interval and self.state == 0:
            self.snake.update()
            self.last_time = current_time

        if self.snake.check_food(self.food):
            self.new_food()
            self.score += 1

        if self.snake.check_death():
            self.state = 1
            self.snake.set_dir(0, 0)
        
    def draw(self):
        self.screen.fill(BACKGROUND)
        pg.draw.rect(self.screen, WHITE, pg.Rect(MARGIN - 2, MARGIN - 2, AREA + 4, AREA + 4), 2)
        self.snake.draw(self.screen)
        pg.draw.rect(self.screen, RED, pg.Rect(self.food.x, self.food.y, SIZE, SIZE))

        if self.state == 1:
            retry_text = self.font.render("PRESS SPACE TO RETRY", True, WHITE)
            self.screen.blit(retry_text, (RES / 2 - retry_text.get_bounding_rect().centerx, RES - 30))

        score_text = self.font.render("SCORE", False, WHITE)
        
        score_text_int = self.font.render(str(self.score), False, WHITE)
        self.screen.blit(score_text, (RES / 2 - score_text.get_bounding_rect().centerx - 15, 7))
        self.screen.blit(score_text_int, (RES / 2 - score_text_int.get_bounding_rect().centerx + 40, 7))

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

                if self.state == 1 and event.key == pg.K_SPACE:
                    self.new_game()

                if event.key == pg.K_ESCAPE:
                    self.should_close = True
                    pg.quit()
                    sys.exit()

    def run(self):
        while not self.should_close:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.new_game()
    game.run()