import pygame
import sys
import os
import random
from openpyxl import Workbook, load_workbook
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * satu_kotak)
            y_pos = int(block.y * satu_kotak)
            block_rect = pygame.Rect(x_pos, y_pos, satu_kotak, satu_kotak)
            pygame.draw.rect(screen, ("#000000"), block_rect)
            
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    def add_block(self):
        self.new_block = True
        

class FRUIT:
    def __init__(self):
       self.randomize()
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * satu_kotak), int(self.pos.y * satu_kotak), satu_kotak, satu_kotak) 
        pygame.draw.rect(screen, ("#FF0043"), fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0, jumlah_kotak - 2)
        self.y = random.randint(0, jumlah_kotak - 2)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
             

pygame.init()

#lebar_display = 600
#tinggi_display = 600
satu_kotak = 30
jumlah_kotak = 20

screen = pygame.display.set_mode((satu_kotak * jumlah_kotak, satu_kotak * jumlah_kotak))
frame_rate = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
    
    screen.fill("#FAC0C0")
    main_game.draw_elements()
    pygame.display.update() 
    frame_rate.tick(5)