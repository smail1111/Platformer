from objects.platforms import Platform, M_Platform, C_Platform
from objects.screen import Screen
from objects.water import Water
from objects.level import Level
from objects.dino import Dino
from constants import *
import pygame

pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dino_sheet_image = pygame.image.load('img/doux.png').convert_alpha()

screen = Screen({
    "platforms":
        [Platform((50, 700), 100, 20),
        Platform((200, 680), 100, 20),
        Platform((450, 600), 120, 20),
        Platform((600, 500), 50, 20),
        Platform((420, 350), 50, 20),
        Platform((600, 200), 50, 20),
        Platform((850, 200), 100, 20),
        Platform((1200, 300), 50, 20)],

    "player": Dino(dino_sheet_image, (50, 600))})

screen_2 = Screen({
    "platforms":
        [Platform((370, 380), 200, 500),
        Platform((300, 500), 200, 500),
        Platform((200, 650), 200, 500),
        Platform((950, 700), 100, 20),
        Platform((1100, 600), 100, 20)],
    
    "player": Dino(dino_sheet_image, (0, 0))}
)

screen_3 = Screen({
    "platforms":
        [Platform((300, 550), 500, 100),
        Platform((20, 600), 500, 100),
        Platform((900, 500), 100, 20),
        Platform((1100, 450), 100, 20, finish=True, color=Yellow),],
    
    "player": Dino(dino_sheet_image, (0, 0))}
)

screen.screen_right = screen_2
screen_2.screen_left = screen
screen_2.screen_right = screen_3
screen_3.screen_left = screen_2

lv = Level(screen)


lv_2_screen = Screen({
    "platforms":
        [Platform((30, 680), 80, 20),
        Platform((150, 600), 800, 20),
        M_Platform((1100, 580), 80, 20, 10, "UD", 10),
        M_Platform((1100, 400), 80, 20, -20, "RL", 10),
        M_Platform((900, 400), 80, 20, -20, "RL", 10),
        M_Platform((700, 400), 80, 20, -20, "RL", 10),
        M_Platform((500, 400), 80, 20, -20, "RL", 10),
        M_Platform((200, 320), 80, 20, 10, "UD", 10),
        M_Platform((100, 160), 80, 20, 10, "UD", 10)],

    "player": Dino(dino_sheet_image, (30, 580))})

lv_2_screen_2 = Screen({
    "platforms":
        [Platform((30, 680), 80, 20),
        M_Platform((200, 600), 150, 20, 20, "UD", 5, True),
        M_Platform((400, 400), 150, 20, -20, "UD", 5, True),
        M_Platform((700, 600), 150, 20, 20, "RL", 5, True),
        M_Platform((1100, 400), 150, 20, -20, "RL", 5, True),
        M_Platform((950, 350), 150, 20, 20, "D-", 5),
        M_Platform((500, 300), 150, 20, 20, "D+", 5),
        Platform((400, 100), 200, 20)],
    
    "player": Dino(dino_sheet_image, (0, 0))})

lv_2_screen_3 = Screen({
    "platforms":
        [Platform((500, 700), 300, 20),
        M_Platform((650, 500), 100, 20, 20, "RL", 6, True),
        M_Platform((350, 600), 100, 20, 20, "RL", 6, True),
        M_Platform((750, 300), 100, 20, -20, "D+", 6, True),
        M_Platform((500, 100), 50, 20, 20, "RL", 6, finish=True, color=Yellow)],
    
    "player": Dino(dino_sheet_image, (0, 0))})

lv_2_screen.screen_up = lv_2_screen_2
lv_2_screen_2.screen_down = lv_2_screen
lv_2_screen_2.screen_up = lv_2_screen_3
lv_2_screen_3.screen_down = lv_2_screen_2

lv2 = Level(lv_2_screen)

lv.next_lv = lv2


lv3_1_tangled_1 = M_Platform((160, 400), 20, 80, 20, "RL", 16, danger=True, color=Red)
lv3_1_tangled_2 = M_Platform((515, 380), 20, 80, -10, "UD", 8, danger=True, color=Red)

lv_3_screen = Screen({
    "platforms":
        [Platform((50, 400), 100, 20),
        Platform((200, 500), 100, 20),
        Platform((400, 500), 100, 20),
        Platform((650, 500), 100, 20),
        Platform((800, 500), 100, 20),
        Platform((950, 500), 100, 20),
        Platform((1100, 500), 100, 20),
        lv3_1_tangled_1,
        lv3_1_tangled_2,
        Platform((765, 380), 20, 80, danger=True, color=Red, tangled=lv3_1_tangled_2),
        Platform((800, 400), 20, 80, danger=True, color=Red, tangled=lv3_1_tangled_1)],
    
    "player": Dino(dino_sheet_image, (50, 300))})

lv3_2_tangled_1 = M_Platform((720, 500), 100, 100, 20, "UD", 10, True, danger=True, color=Red)

lv_3_screen_2 = Screen({
    "platforms":
        [Platform((50, 600), 100, 20),
        Platform((300, 600), 100, 20),
        Platform((400, 480), 100, 20),
        Platform((600, 450), 100, 20),
        Platform((800, 600), 100, 20),
        Platform((1000, 510), 100, 20),
        Platform((900, 350), 100, 20),
        Platform((1050, 200), 100, 20),
        Platform((1100, 100), 100, 20),
        lv3_2_tangled_1,
        Platform((1040, 500), 100, 100, 20, danger=True, color=Red, tangled=lv3_2_tangled_1),
        Platform((400, 500), 100, 100, 20, danger=True, color=Red, tangled=lv3_2_tangled_1)],
    
    "player": Dino(dino_sheet_image, (0, 0))})

lv3_3_tangled_1 = M_Platform((650, 680), 200, 20, -10, "RL", 20)
lv3_3_tangled_2 = M_Platform((875, 620), 20, 80, 5, "UD", 20, danger=True, color=Red, tangled=lv3_3_tangled_1)
lv3_3_tangled_3 = M_Platform((870, 300), 20, 80, -12.5, "RL", 20, danger=True, color=Red, tangled=lv3_3_tangled_1)

lv_3_screen_3 = Screen({
    "platforms":
        [Platform((900, 680), 100, 20),
         Platform((10, 510), 100, 20),
         lv3_3_tangled_1,
         lv3_3_tangled_2,
         lv3_3_tangled_3,
         Platform((300, 680), 200, 20, tangled=lv3_3_tangled_1),
         Platform((300, 400), 200, 20, tangled=lv3_3_tangled_1),
         Platform((650, 400), 200, 20, tangled=lv3_3_tangled_1),
         Platform((565, 620), 20, 80, danger=True, color=Red, tangled=lv3_3_tangled_2),
         Platform((520, 300), 20, 80, danger=True, color=Red, tangled=lv3_3_tangled_3),
         Platform((900, 350), 100, 20, color=Yellow, finish=True)],
    
    "player": Dino(dino_sheet_image, (0, 0))})

lv_3_screen.screen_right = lv_3_screen_2
lv_3_screen_2.screen_left = lv_3_screen
lv_3_screen_2.screen_up = lv_3_screen_3
lv_3_screen_3.screen_down = lv_3_screen_2

lv3 = Level(lv_3_screen)

lv2.next_lv = lv3


player_jumps = lambda objs: objs["player"].jumping

lv4_screen = Screen({
    "platforms": 
        [Platform((50, 575), 100, 20),
         C_Platform((200, 650), 100, 20, player_jumps, True, color=DarkBlue),
         C_Platform((350, 425), 100, 20, player_jumps, True, color=DarkBlue),
         C_Platform((550, 425), 100, 20, player_jumps, True, color=DarkBlue),
         C_Platform((780, 600), 100, 20, player_jumps, True, color=DarkBlue),
         C_Platform((1100, 500), 100, 20, player_jumps, True, color=DarkBlue),
         C_Platform((200, 500), 100, 20, player_jumps, True, start=False, color=DarkRed),
         C_Platform((350, 575), 100, 20, player_jumps, True, start=False, color=DarkRed),
         C_Platform((850, 450), 100, 20, player_jumps, True, start=False, color=DarkRed),
         C_Platform((1050, 450), 100, 20, player_jumps, True, start=False, color=DarkRed),
         C_Platform((700, 200), 20, 200, player_jumps, True, start=False, danger=True, color=Red),
         C_Platform((1200, 200), 20, 200, player_jumps, True, start=False, danger=True, color=Red)],
    
    "player": Dino(dino_sheet_image, (50, 475))})

lv4_2_tangled_1 = M_Platform((0, 0), 0, 0, 20, "RL", 40)

lv4_screen_2 = Screen({
    "platforms": 
        [Platform((50, 575), 100, 20),
         Platform((1080, 400), 100, 20),
         lv4_2_tangled_1,
         C_Platform((100, 520), 150, 20, player_jumps, True, start=False, color=DarkRed, tangled=lv4_2_tangled_1),
         C_Platform((250, 520), 150, 20, player_jumps, True, color=DarkBlue, tangled=lv4_2_tangled_1),
         C_Platform((400, 300), 20, 200, player_jumps, True, start=False, danger=True, color=Red),
         C_Platform((800, 300), 20, 200, player_jumps, True, start=False, danger=True, color=Red),
         C_Platform((200, 300), 20, 200, player_jumps, True, danger=True, color=Red),
         C_Platform((600, 300), 20, 200, player_jumps, True, danger=True, color=Red),
         C_Platform((1000, 300), 20, 200, player_jumps, True, danger=True, color=Red)],
    
    "player": Dino(dino_sheet_image, (0, 0))})

lv4_3_tangled_1 = M_Platform((0, 0), 0, 0, 20, "UD", 15)
lv4_3_tangled_2 = M_Platform((0, 0), 0, 0, -20, "UD", 15)

lv4_screen_3 = Screen({
    "platforms": 
        [Platform((50, 575), 100, 20),
         lv4_3_tangled_1,
         lv4_3_tangled_2,
         C_Platform((200, 620), 100, 20, player_jumps, True, start=False, color=DarkRed, tangled=lv4_3_tangled_1),
         C_Platform((400, 220), 100, 20, player_jumps, True, start=False, color=DarkRed, tangled=lv4_3_tangled_2),
         C_Platform((600, 620), 100, 20, player_jumps, True, start=False, color=DarkRed, tangled=lv4_3_tangled_1),
         C_Platform((800, 220), 100, 20, player_jumps, True, start=False, color=DarkRed, tangled=lv4_3_tangled_2),
         C_Platform((1000, 320), 100, 20, player_jumps, True, finish=True, color=Yellow)],
    
    "player": Dino(dino_sheet_image, (0, 0))})

lv4_screen.screen_right = lv4_screen_2
lv4_screen_2.screen_left = lv4_screen
lv4_screen_2.screen_right = lv4_screen_3
lv4_screen_3.screen_left = lv4_screen_2

lv4 = Level(lv4_screen)

lv3.next_lv = lv4


lv5_1_tangled_1 = M_Platform((0, 0), 0, 0, -10, "UD", 30)
lv5_1_tangled_2 = M_Platform((0, 0), 0, 0, 10, "UD", 30)
lv5_1_tangled_3 = M_Platform((0, 0), 0, 0, 10, "RL", 15)

lv_5_screen = Screen({
    "platforms":
        [Platform((50, 650), 100, 20)],
    
    "water":
        [lv5_1_tangled_1,
        lv5_1_tangled_2,
        lv5_1_tangled_3,
        Water((200, 500), 50, 200),
        Water((200, 300), 200, 50, tangled=lv5_1_tangled_3),
        Water((750, 250), 200, 50, tangled=lv5_1_tangled_1),
        Water((1050, 600), 200, 50, tangled=lv5_1_tangled_2)],

    "player": Dino(dino_sheet_image, (50, 550))})

lv5_2_tangled_1 = M_Platform((0, 0), 0, 0, 10, "RL", 70)

lv_5_screen_2 = Screen({
    "platforms":
        [Platform((100, 600), 100, 20),
         Platform((1100, 600), 100, 20),
         Platform((220, 20), 800, 20, danger=True, color=Red),
         Platform((400, 680), 800, 20, danger=True, color=Red), 
         Platform((220, 40), 20, 360, danger=True, color=Red),
         Platform((400, 320), 20, 360, danger=True, color=Red),
         Platform((600, 40), 20, 360, danger=True, color=Red),
         Platform((800, 320), 20, 360, danger=True, color=Red),
         Platform((1000, 40), 20, 360, danger=True, color=Red)],
    
    "water":
        [lv5_2_tangled_1,
         Water((220, 40), 100, 640, tangled=lv5_2_tangled_1)],

    "player": Dino(dino_sheet_image, (0, 0))})

lv5_3_tangled_1 = M_Platform((0, 0), 0, 0, 10, "RL", 70)

lv_5_screen_3 = Screen({
    "platforms":
        [Platform((100, 600), 100, 20),
         Platform((1100, 450), 100, 20),
         M_Platform((250, 220), 100, 20, -10, "UD", 20, danger=True, color=Red, tangled=lv5_3_tangled_1),
         M_Platform((250, 475), 100, 20, -10, "UD", 20, danger=True, color=Red, tangled=lv5_3_tangled_1),
         Platform((100, 150), 100, 20, finish=True, color=Yellow)],
    
    "water":
        [lv5_3_tangled_1,
         Water((250, 222), 100, 470, tangled=lv5_3_tangled_1)],

    "player": Dino(dino_sheet_image, (0, 0))})

lv_5_screen.screen_right = lv_5_screen_2
lv_5_screen_2.screen_left = lv_5_screen
lv_5_screen_2.screen_right = lv_5_screen_3
lv_5_screen_3.screen_left = lv_5_screen_2

lv5 = Level(lv_5_screen)

lv4.next_lv = lv5
# I should probably place each of these levels in their own files at a certain point rather than doing this.