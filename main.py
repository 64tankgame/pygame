import pygame
import sys
width=1100
height=650
class player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.image.load('tank/tank_u.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
    


    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x-=5
            if self.rect.left<=0:
                self.rect.left=0
        if keys[pygame.K_RIGHT]:
            self.rect.x+=5
            if self.rect.right>=width:
                self.rect.right=width
        if keys[pygame.K_UP]:
            self.rect.y-=5
            if self.rect.top<=0:
                self.rect.top=0
        if keys[pygame.K_DOWN]:
            self.rect.y+=5
            if self.rect.bottom>=height:
                self.rect.bottom=height   
    
 
   

        
class Game():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('my game')
        self.all_sprites=pygame.sprite.Group()
        self.player = player(width // 2, height // 2)
        self.all_sprites.add(self.player)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.all_sprites.update()
            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            
# if __name__=='__dottry__':
#     game = Game()
#     game.run()
game = Game()
game.run()



def main():
    #pygame初始化
    pygame.init()

    # 窗口標題
    pygame.display.set_caption('以python顯示圖片')

    #設定視窗
    screen=pygame.display.set_mode((width,height))

    #建立clock
    clock=pygame.time.Clock()

    img_background = pygame.image.load('c:/Users/User/Documents/pygame/all white .png')
    img_background = pygame.transform.scale(img_background,[910,540])
    tmr=0
    class chara:
        def __init__(self,x,y,hp,direction):
            
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5
                
    #width, height = 500, 500                   #遊戲畫面寬和高
    '''screen = pygame.display.set_mode((width, height))   #依設定顯示視窗
    pygame.display.set_caption("Test")                  #設定程式標題
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)
    tmr = 0
    img_bg = pygame.image.load("background.jpg")
    '''
    
    #關閉程式的程式碼
    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#按下x
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
            if event.key == pygame.K_ESCAPE:
                screen = pygame.display.set_mode((width, height))
            
        x=tmr%160
        screen.blit(img_background,[0,0])
        '''for i in range(5):
           screen.blit(img_background,[i*3840-x,0])    
        #txt = font.render(str(tmr),True,white)
        #screen.blit(img_bg,[0,0])
        #screen.blit(txt , [125,125])
        '''
        pygame.display.update()
        clock.tick(5)
                   
                

if __name__ == '__main__':
    main()
