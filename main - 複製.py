#匯入pygame
import pygame as pygame
import sys

white = (255,255,255)
black = (0,0,0)
cyan = (0,255,255)



def main():
    #pygame初始化
    pygame.init()

    #設定視窗
    
    width, height = 800, 589                    #遊戲畫面寬和高
    screen = pygame.display.set_mode((width, height))   #依設定顯示視窗
    pygame.display.set_caption("Test")                  #設定程式標題
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)
    tmr = 0
    img_bg = pygame.image.load("background.jpg")
    #關閉程式的程式碼
    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
            if event.key == pygame.K_ESCAPE:
                screen = pygame.display.set_mode((width, height))
            

        txt = font.render(str(tmr),True,white)
        screen.blit(img_bg,[0,0])
        screen.blit(txt , [125,125])
        
        pygame.display.update()
        clock.tick(10)
                    

#if __name__ == '_main_':
main()
