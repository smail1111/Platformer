from levels import lv, lv2, lv3, lv4, lv5, display
from objects.button import Button
from objects.level import Level
from constants import BG, FPS
import pygame

pygame.display.set_caption("Platformer")

#Load Images
start_btn_image = pygame.image.load("img/start_btn.png").convert_alpha()
exit_btn_image = pygame.image.load("img/exit_btn.png").convert_alpha()
level_btn_image = pygame.image.load("img/level_btn.png").convert_alpha()

back_btn_image = pygame.image.load("img/back_btn.png").convert_alpha()
one_btn_image = pygame.image.load("img/one_btn.png").convert_alpha()
two_btn_image = pygame.image.load("img/two_btn.png").convert_alpha()
three_btn_image = pygame.image.load("img/three_btn.png").convert_alpha()
four_btn_image = pygame.image.load("img/four_btn.png").convert_alpha()
five_btn_image = pygame.image.load("img/five_btn.png").convert_alpha()

#Create Buttons
start_btn = Button(285, 300, start_btn_image)
exit_btn = Button(730, 300, exit_btn_image)
levels_btn = Button(500, 500, level_btn_image)

back_btn = Button(500, 500, back_btn_image)
one_btn = Button(275, 300, one_btn_image)
two_btn = Button(425, 300, two_btn_image)
three_btn = Button(575, 300, three_btn_image)
four_btn = Button(725, 300, four_btn_image)
five_btn = Button(875, 300, five_btn_image)

#Show Menus
def main() -> None:
    show_levels = False
    show_levels = False
    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                return
        display.fill(BG)

        levels_btn.draw(display)
        start_btn.draw(display)
        exit_btn.draw(display)

        if start_btn.get_clicked():
            run_platformer(lv)
            return
        
        #Show Levels
        while show_levels:
            display.fill(BG)

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    return
            
            one_btn.draw(display)
            two_btn.draw(display)
            three_btn.draw(display)
            four_btn.draw(display)
            five_btn.draw(display)
            back_btn.draw(display)

            if one_btn.get_clicked():
                run_platformer(lv)
                return

            if two_btn.get_clicked():
                run_platformer(lv2)
                return

            if three_btn.get_clicked():
                run_platformer(lv3)
                return

            if four_btn.get_clicked():
                run_platformer(lv4)
                return

            if five_btn.get_clicked():
                run_platformer(lv5)
                return

            if back_btn.get_clicked():
                levels_btn.clicked = True
                show_levels = False

            pygame.display.update()

        #Switch To Levels
        if levels_btn.get_clicked():
            back_btn.clicked = True
            show_levels = True
        
        if exit_btn.get_clicked():
            break
        
        pygame.display.update()

#Run Level
def run_platformer(lv: Level) -> None:
    clock = pygame.time.Clock()
    current_lv = lv
    dt = 0.0
    
    while True:   
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            current_lv.reset()
            main()
            return

        current_lv.update(dt)
        current_lv.draw(display)
        
        if current_lv.complete:
            current_lv.reset()
            if current_lv.next_lv is not None:
                current_lv = current_lv.next_lv
            else:   
                main()
                return
        
        pygame.display.update()
        dt = clock.tick(FPS) / 100

#Call Main
main()