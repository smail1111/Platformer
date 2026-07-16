from levels import lv, lv2, lv3, lv4, display
from objects.button import Button
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

#Create Buttons
start_btn = Button(285, 300, start_btn_image)
exit_btn = Button(730, 300, exit_btn_image)
levels_btn = Button(500, 500, level_btn_image)

back_btn = Button(500, 500, back_btn_image)
one_btn = Button(300, 300, one_btn_image)
two_btn = Button(450, 300, two_btn_image)
three_btn = Button(600, 300, three_btn_image)
four_btn = Button(750, 300, four_btn_image)


def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
        display.fill("lightblue")
  
        levels_btn.draw(display)
        start_btn.draw(display)
        exit_btn.draw(display)

        if start_btn.get_clicked():
            running = False
            run_platformer(lv)
            break
        
        
        def show_levels():
            running = True
            
            while running:
                display.fill("lightblue")

                for event in pygame.event.get():
                    if event.type is pygame.QUIT:
                        running = False
                
                one_btn.draw(display)
                two_btn.draw(display)
                three_btn.draw(display)
                four_btn.draw(display)
                back_btn.draw(display)

                if one_btn.get_clicked():
                    running = False
                    run_platformer(lv)
                    break

                if two_btn.get_clicked():
                    running = False
                    run_platformer(lv2)
                    break

                if three_btn.get_clicked():
                    running = False
                    run_platformer(lv3)
                    break

                if four_btn.get_clicked():
                    running = False
                    run_platformer(lv4)
                    break

                if back_btn.get_clicked():
                    running = False
                    levels_btn.clicked = True
                    main()
                    break

                pygame.display.update()

        
        if levels_btn.get_clicked():
            back_btn.clicked = True
            running = False
            show_levels()
            break
        
        if exit_btn.get_clicked():
            running = False
            break
        
        pygame.display.update()


def run_platformer(lv):
    current_lv = lv
    dt = 0.0
    clock = pygame.time.Clock()
    running = True
    
    while running:   
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            current_lv.reset()
            running = False
            main()
            break

        current_lv.update(dt)
        current_lv.draw(display)
        if current_lv.complete:
            current_lv.reset()
            if current_lv.next_lv is not None:
                current_lv = current_lv.next_lv
            else:   
                running = False
                main()
                break
        
        pygame.display.update()
        dt = clock.tick(60) / 100

main()