import pygame
from screen import Screen
from platform import Platform
from level import Level
from dino import Dino
from button import Button
from constants import *

pygame.init()

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

dino_sheet_image = pygame.image.load('img/doux.png').convert_alpha()
start_btn_image = pygame.image.load("img/start_btn.png").convert_alpha()
exit_btn_image = pygame.image.load("img/exit_btn.png").convert_alpha()

start = Button(350, 300, start_btn_image)
exit = Button(750, 300, exit_btn_image)

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
        
        display.fill("lightblue")
        start.draw(display)
        exit.draw(display)
        
        if start.get_clicked():
            run_platformer()
            running = False
        if exit.get_clicked():
            running = False
        
        pygame.display.update()

def run_platformer():
    screen = Screen([
        [Platform((50, 700), 100, 20),
         Platform((200, 680), 100, 20),
         Platform((450, 600), 120, 20),
         Platform((600, 500), 50, 20),
         Platform((420, 350), 50, 20),
         Platform((600, 200), 50, 20),
         Platform((850, 200), 100, 20),
         Platform((1200, 300), 50, 20)],
        [Dino(dino_sheet_image, (50, 600))]])

    screen_2 = Screen([
        [Platform((370, 380), 200, 500),
         Platform((300, 500), 200, 500),
         Platform((200, 650), 200, 500),
         Platform((950, 700), 100, 20),
         Platform((1100, 600), 100, 20),],
        [Dino(dino_sheet_image, (0, 0))]]
    )

    screen_3 = Screen([
        [Platform((300, 550), 500, 100),
         Platform((20, 600), 500, 100),
         Platform((900, 500), 100, 20),
         Platform((1100, 450), 100, 20, finish=True, color="yellow"),],
        [Dino(dino_sheet_image, (0, 0))]]
    )

    screen.screen_right = screen_2
    screen_2.screen_left = screen
    screen_2.screen_right = screen_3
    screen_3.screen_left = screen_2

    lv = Level(screen)
    
    lv_2_screen = Screen([[
        Platform((30, 680), 80, 20),
        Platform((150, 600), 800, 20),
        Platform((1100, 580), 80, 20, 20, "UD", 6),
        Platform((1100, 400), 80, 20, -20, "RL", 10),
        Platform((900, 400), 80, 20, -20, "RL", 10),
        Platform((700, 400), 80, 20, -20, "RL", 10),
        Platform((500, 400), 80, 20, -20, "RL", 10),
        Platform((200, 300), 80, 20, -20, "UD", 5),
        Platform((100, 200), 80, 20, 20, "UD", 5),
    ],
        [Dino(dino_sheet_image, (30, 580))]])
    
    lv_2_screen_2 = Screen([[
        Platform((30, 680), 80, 20),
        Platform((200, 600), 150, 20, 20, "UD", 5, True),
        Platform((400, 400), 150, 20, -20, "UD", 5, True),
        Platform((700, 600), 150, 20, 20, "RL", 5, True),
        Platform((1100, 400), 150, 20, -20, "RL", 5, True),
        Platform((950, 350), 150, 20, 20, "D-", 5),
        Platform((500, 300), 150, 20, 20, "D+", 5),
        Platform((400, 100), 250, 20)
    ],
        [Dino(dino_sheet_image, (30, 580))]])
    
    lv_2_screen_3 = Screen([[
        Platform((500, 700), 300, 20),
        Platform((650, 500), 100, 20, 20, "RL", 6, True),
        Platform((350, 600), 100, 20, 20, "RL", 6, True),
        Platform((750, 300), 100, 20, -20, "D+", 6, True),
        Platform((500, 100), 50, 20, 20, "RL", 6, finish=True, color="yellow"),
    ],
        [Dino(dino_sheet_image, (500, 600))]])
    
    lv_2_screen.screen_up = lv_2_screen_2
    lv_2_screen_2.screen_down = lv_2_screen
    lv_2_screen_2.screen_up = lv_2_screen_3
    lv_2_screen_3.screen_down = lv_2_screen_2

    lv2 = Level(lv_2_screen)

    lv.next_lv = lv2

    current_lv = lv

    running = True
    
    dt = 0.0
    clock = pygame.time.Clock()

    
    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False

        current_lv.update(dt)
        current_lv.draw(display)
        
        if lv.complete and current_lv.next_lv:
            current_lv = current_lv.next_lv

        current_lv.draw(display)
        
        pygame.display.update()
        dt = clock.tick(60) / 100

main()