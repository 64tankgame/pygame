from setting import *
from tank import TANK_P1,TANK_P2
from feild import *
from txtrander import *


#pygame.display.set_icon(game_icon_img)


def draw_map():
    for row in range(map_row):
        for col in range(map_col):
            if map[row][col] == 1:
                pygame.draw.rect(game_screen,(0,0,0),(col * block_size, row * block_size, block_size, block_size))
def main():
    clock = pygame.time.Clock()
    running = True
    paused = False
    
    
    tankp1 = TANK_P1(WIDTH/2-300,HEIGHT/2)
    player_sprite.add(tankp1)
    
    tankp2 = TANK_P2(WIDTH/2+300,HEIGHT/2)
    player_sprite.add(tankp2)
    
    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Toggle the pause state when the Esc key is pressed
                    paused = not paused
        if paused:
            continue
        
        keys = pygame.key.get_pressed()
        
        
        player_sprite.update()
        shell_sprite.update()
        
        background = pygame.Surface((WIDTH, HEIGHT))
        background.fill((255, 255, 255)) # Fill the surface with white color
        game_screen.blit(background, (0, 0)) # Draw the background onto the game screen at position (0, 0)
        

        # game_screen.blit(txt,txtrext)

        # draw_map()

        player_sprite.draw(game_screen)
        turrent_sprite.draw(game_screen)
        shell_sprite.draw(game_screen)
        bar_sprite.draw(game_screen)
        
        pygame.display.update()


if __name__ == '__main__':
    main()