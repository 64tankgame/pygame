import pygame
import sys
from bullet import Bullet
width=1300
height=750
speed = 2
all_bullet_sprite = pygame.sprite.Group()
time_tank_1_attack = 0
cooldown_tank_1 = 0

class player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.image.load('tank/tank_u.png')
        self.image_p= pygame.image.load('tank/tank_u.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rotate_direction = 0
    

    def update(self):
        global time_tank_1_attack

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rotate_direction != 3:
                self.rotate_direction = 3
                self.image = pygame.transform.rotate(self.image_p, 90)

        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
            if self.rect.right>=width:
                self.rect.right=width
            if self.rotate_direction != 1:
                self.rotate_direction = 1
                self.image = pygame.transform.rotate(self.image_p, -90)

        if keys[pygame.K_UP]:
            self.rect.y -= speed
            if self.rect.top<=0:
                self.rect.top=0
            if self.rotate_direction != 0:
                self.rotate_direction = 0
                self.image = pygame.transform.rotate(self.image_p, 0)
        
        if keys[pygame.K_DOWN]:
            self.rect.y += speed
            if self.rect.bottom>=height:
                self.rect.bottom=height
            if self.rotate_direction != 2:
                self.rotate_direction = 2
                self.image = pygame.transform.rotate(self.image_p, 180)
        
        if keys[pygame.K_SPACE]:
            if time_tank_1_attack <= 0: 
                bullet = Bullet(self.rect.centerx,self.rect.centery,self.rotate_direction,0)
                all_bullet_sprite.add(bullet)
                time_tank_1_attack = 200

        if time_tank_1_attack >= 0 :
            time_tank_1_attack -= 1        


    
class Game():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('my game')
        self.all_sprites=pygame.sprite.Group()
        self.player = player(width // 2, height // 2)
        self.all_sprites.add(self.player)

    def run(self):
        clock=pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.all_sprites.update()
            all_bullet_sprite.update()
            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)
            all_bullet_sprite.draw(self.screen)
            clock.tick(144)
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
            self.image = pygame.image.load('c:/Users/User/Documents/pygame/ dot.jpg')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.direction = "up" #方向
            self.tank_all_image= self.image.subsurface((0, 0), (48, 48))
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

        def update_direction(self):
       
            if  self.direction == 'up':
                self.tank_all_image = self.image.subsurface((0, 0), (48, 48))
                self.image_postion_index = 0

            elif self.direction == 'down':
                self.tank_all_image = self.image.subsurface((0, 48), (48, 48))
                self.image_postion_index = 48
            elif self.direction == 'left':
                self.tank_all_image = self.image.subsurface((0, 96), (48, 48))
                self.image_postion_index = 96
            elif self.direction == 'right':
                self.tank_all_image = self.image.subsurface((0, 144), (48, 48))
                self.image_postion_index = 144


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
        clock.tick(60)
                   
                

if __name__ == '__main__':
    main()
