import pygame as pg
from settings import *

class Snake:
    def __init__(self):
        self.body = []
        self.body.extend([pg.Vector2(80, 220), pg.Vector2(100, 220), pg.Vector2(120, 220)])
        print(self.body)
        self.length = 2

        self.x_dir = 0
        self.y_dir = 0

        self.grow = False

    def update(self):
        if self.x_dir != 0 or self.y_dir != 0:
            head_x = self.body[-1].x
            head_y = self.body[-1].y

            self.body.append(pg.Vector2(head_x + self.x_dir * SIZE, head_y + self.y_dir * SIZE))

            if not self.grow:
                self.body.pop(0)
            else:
                self.grow = False
                self.length += 1

    def check_food(self, food):
        if self.body[-1] == food:
            self.grow = True
            # print(self.body)
            return True
        
        return False
    
    def check_death(self):
        if self.body[-1].x < MARGIN or self.body[-1].x >= RES - MARGIN:
            self.body.pop()
            return True
        
        if self.body[-1].y < MARGIN or self.body[-1].y >= RES - MARGIN:
            self.body.pop()
            return True
        
        for segment in self.body[:-1]:
            if segment == self.body[-1]:
                return True
        
        return False

    def draw(self, screen):
        for segment in self.body:    
            pg.draw.rect(screen, GREEN, pg.Rect(segment.x, segment.y, SIZE, SIZE))

    def set_dir(self, x, y):
        self.x_dir = x
        self.y_dir = y

    def get_dir(self):
        return (self.x_dir, self.y_dir)
    
    def get_length(self):
        return self.length
    
    def get_body(self):
        return self.body